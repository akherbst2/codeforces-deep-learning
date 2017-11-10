from bs4 import BeautifulSoup
import os
import sys
import urllib
import urllib.request
import re
text_path = 'texts/{}'
num_pages = 38

try:
    os.makedirs(text_path.format(''))
except OSError:
    print('text folder prepared.')


def import_cf():
    if not len(sys.argv) < 2:
        print("Usage: %s <URL>" % (sys.argv[0]))
        print('invalid')
        sys.exit(1)

    for i in range(1, num_pages + 1):
        url = 'http://codeforces.com/problemset/page/{}'.format(i)
        f = urllib.request.urlopen(url)
        soup = BeautifulSoup(f, "lxml")
        for pages in soup.findAll('a', attrs={'href': re.compile(r'/problemset/problem/[a-zA-Z0-9]*/[a-zA-Z]*')}):
            try:
                full_url = urllib.parse.urljoin(url, pages['href'])
                print("URL: ", full_url)
                split = full_url.split('/')

                text_filename = '{}{}.txt'.format(split[-2], split[-1])
                urllib.request.urlretrieve(
                    full_url, text_path.format(text_filename))
            except Exception as e:
                print('invalid link: {}'.format(e))


def main():
    import_cf()


if __name__ == '__main__':
    main()
