
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
(or alternatively, in bash shell)
```
  $ source activate python3.5
```
<<<<<<< HEAD
  $ python scraper.py
```
=======
If you would like to deactivate the virtual environment, run
```
  $ deactivate
```

## Install dependencies:
While your python virtual environment is activated, run
```
  $ pip install -r requirements
```

## Training the Neural Network
To run, activate your python virtual environment and open jupyter notebook from an Anaconda shell.  Note that if you are running this through a laptop, the training runs significantly faster if your laptop is plugged into a power source.

(in Anaconda shell)
```
  $ activate python3.5
  $ jupyter notebook
```  
This should open up a browser window for jupyter notebook.  Open up please_work.ipynb and step through every code block.

---------------------------------------
##Codeforces Scraper info.
The codebase obtains the Codeforces problems by using the BeautifulSoup library. Some instructions are below.

## Running the Scraper
This should not be necessary because we already have a database in our github repo.  However, if you want to download the latest Codeforces data, this is how you scrape the data.

**NOTE: Running the scraper may be very disruptive towards Codeforces contests hosted on the website!! In order to not be a jerk, please check http://codeforces.com/contests/ to ensure that there is currently not a contest going on.  Also note that the start time listed on the website may not be in your time zone.  Click on the DATE itself (i.e. "Dec/12/2017 10:05UTC-5") to view when the contest has started in YOUR timezone.**

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
