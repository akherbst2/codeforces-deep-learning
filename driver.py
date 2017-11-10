import os
import sys, urllib, re
import urllib.request
from bs4 import BeautifulSoup
text_path = 'texts/{}.txt'
num_pages = 1

os.makedirs(text_path.format(''))


def import_cf():
    if not len(sys.argv) < 2:
        print("Usage: %s <URL>" % (sys.argv[0]))
        print('invalid')
        sys.exit(1)

    url = 'http://codeforces.com/problemset/page/1'
    f = urllib.request.urlopen(url)
    soup = BeautifulSoup(f, "lxml")
    for i in soup.findAll('a', attrs={'href': re.compile(r'/problemset/problem/[a-zA-Z0-9]*/[a-zA-Z]*')}):
        try:
            full_url = urllib.parse.urljoin(url, i['href'])
            print("pdf URL: ", full_url)
            split = full_url.split('/')

            text_filename = '{}{}'.format(split[-2], split[-1])
            urllib.request.urlretrieve(full_url, text_path.format(text_filename))
        except Exception as e:
            print('invalid link: {}'.format(e))


def main():
    import_cf()

if __name__ == '__main__': main()
