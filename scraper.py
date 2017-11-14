from bs4 import BeautifulSoup
import os
import pickle
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

        raw_html_pages_by_id = dict()

        for pages in soup.findAll('a', attrs={'href': re.compile(r'/problemset/problem/[a-zA-Z0-9]*/[a-zA-Z]*')}):
            excess_url = pages['href']
            trunc = "/problem/"
            index = excess_url.find("/problem/")
            id = excess_url[index + len(trunc):]
            try:
                full_url = urllib.parse.urljoin(url, pages['href'])
                print("URL: ", full_url)

                page = urllib.request.urlopen(full_url)

                raw_html_pages_by_id[id] = (page.read())

            except Exception as e:
                print('invalid link: {}'.format(e))

        print("Dumping batch ", i)
        for k, v in raw_html_pages_by_id.items():
            text_path = 'texts/{}'.format(k) + ".html"
            os.makedirs(os.path.dirname(text_path), exist_ok=True)
            with open(text_path, 'wb') as outfile:
                outfile.write(v)






class Problem:

    def __init__(self):
        self.title = ''
        self.time_limit = ''
        self.memory_limit = ''
        self.main_text = ''
        self.input_specification = ''
        self.output_specification = ''

    def __str__(self):
        return self.title

def main():
    import_cf()


if __name__ == '__main__':
    main()
