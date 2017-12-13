The codebase obtains the Codeforces problems by using the BeautifulSoup library. Some instructions are below.

# codeforces-scraper

Install dependencies:
```
  $ pip install beautifulsoup4
```
To run,
```
  $ python scraper.py
```
This should download every html page to every problem on Codeforces to directory called
"texts" in your current directory. Within "texts", the files will be organized in subdirectories based on the contest.

NOTE: When running the scraper, please do not run during peak hours (i.e., especially not during or near the time of a
Codeforces contest). The site experiences a lot of load during the contests as is. Also, the scraper would almost
certainly run slower as well.

To avoid running the scraper unnecessarily, a zip file with the first 3800 or so problems is included in the repo. Of
course, recent and future problems are not included.

problem.py contains a class object that will represent fields for a single problem.

To load all problems, see the util.loadAllProblems() function. This will parse the raw html from the scraper output
into a set of problem objects.

