# Codeforces Learner

## Setup

### Glibc
This project requires glibc version >= 2.16.  To check which version you have, run
```
  $ ldd --version
```
If you don't have the correct version, I recommend running this software on a different computer.  Updating glibc is a long and painful process, and has the potential to mess things up on your computer.  However, if you do want to update glibc, there are many tutorials online, and it can differ per operating system.  This project worked on Windows 10, using Anaconda, but did not work on CentOS 6.8, using Anaconda.

### Anaconda
We recommend you use Anaconda to run this project.  Download here:  https://www.anaconda.com/download/

### Python
Requires Python 3, recommended use is Python 3.5.  We also recommend you use a virtual environment to download requirements and run.  To set up a virtual environment, run

(via Anaconda shell)
```
  $ conda create -n python3.5 python=3.5 
```

Then to activate the python virtual environment, run

(in Anaconda shell)
```
  $ activate python3.5
```
(in bash shell)
```
  $ source activate python3.5
```



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
