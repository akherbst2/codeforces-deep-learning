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

    # for i in range(1, num_pages + 1):
    i = 1
    url = 'http://codeforces.com/problemset/page/{}'.format(i)
    f = urllib.request.urlopen(url)
    soup = BeautifulSoup(f, "lxml")

    problems = []

    for pages in soup.findAll('a', attrs={'href': re.compile(r'/problemset/problem/[a-zA-Z0-9]*/[a-zA-Z]*')}):
        try:
            full_url = urllib.parse.urljoin(url, pages['href'])
            print("URL: ", full_url)

            page = urllib.request.urlopen(full_url)
            page_soup = BeautifulSoup(page, "lxml")

            new_problem = Problem()
            new_problem.title = page_soup.find(attrs={'class': 'title'}).text
            new_problem.time_limit = page_soup.find(
                attrs={'class': 'time-limit'}).text.split('time limit per test')[1]
            new_problem.memory_limit = page_soup.find(
                attrs={'class': 'memory-limit'}).text.split('memory limit per test')[1]
            new_problem.main_text = page_soup.find(
                attrs={'class': 'header'}).next_sibling.text
            new_problem.input_specification = page_soup.find(
                attrs={'class': 'input-specification'}).text.split('Input')[1]
            new_problem.output_specification = page_soup.find(
                attrs={'class': 'output-specification'}).text.split('Output')[1]
            new_problem.tags = new_problem.output_specification = page_soup.find(
                attrs={'class': 'tag-box'}).text
            print(new_problem.tags)
            problems.append(new_problem)
        except Exception as e:
            print('invalid link: {}'.format(e))
    with open('output.pkl', 'wb') as outfile:
        pickle.dump(problems, outfile, protocol=pickle.HIGHEST_PROTOCOL)


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
