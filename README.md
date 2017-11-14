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

problem.py contains a class object that will represent fields for a single problem.

To load all problems, see the util.loadAllProblems() function.