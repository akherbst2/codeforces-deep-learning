
"""
This file contains many data parsing functions. Many of them are meant to be run once and leave a more refined data
file. A variety of changes to the formatting have occurred over time, but the old formatting functions are still in
this file in case they become useful later.
"""

import os
import problem
from collections import Counter
import random

#Canabalized from https://stackoverflow.com/questions/32910096/is-there-a-way-to-auto-generate-a-str-implementation-in-python
def stringify(thingy):
    attributes = dir(thingy)
    res = thingy.__class__.__name__ + "(\n"
    first = True
    for attr in attributes:
        if attr.startswith("__") and attr.endswith("__"):
            continue
        if callable(getattr(thingy, attr)):
            continue
        res += attr + " = " + str(getattr(thingy, attr))
        res += "\n"

    res += ")"
    return res

"""Given an instance of the Problem class, computes a header line for a csv. Uses the variable names in code of
the Problem class."""
def CSVHeaderString(problem):
    attributes = dir(problem)
    headers = []
    for attr in attributes:
        if attr.startswith("__") and attr.endswith("__"):
            continue
        if callable(getattr(problem, attr)):
            continue
        headers.append(attr)
    return ",".join(headers)

"""Given an instance of the Problem class, outputs a comma separated line of its fields. If the fields already
had commas, this could be a problem, so such commas are replaced by '/'  """
def CSVItemString(problem):
    attributes = dir(problem)
    headers = []
    for attr in attributes:
        if attr.startswith("__") and attr.endswith("__"):
            continue
        if callable(getattr(problem, attr)):
            continue
        #headers.append(problem.sanitize(str(getattr(problem, attr))))
        headers.append((str(getattr(problem, attr))).replace(",", "/"))
    return ",".join(headers)


"""Creates and writes a csv file containing all the given problem info
First line of csv will have header info
CSV fields will have strings of the format given by str(field), with commas replaced by '/' """

def outputCSV(problems, text_path):
    if (len(problems) == 0):
        print("Error, empty list sent as input to outputCSV function")
        return ""
    with open(text_path, 'wb') as outfile:
        header = (CSVHeaderString(problems[0]) + "\n")
        outfile.write(header.encode('utf8'))
        for problem in problems:
            line = CSVItemString(problem) + "\n"
            outfile.write(line.encode('utf8'))

"""
Return list of Problem class objects. Roughly 4000
"""
def loadAllProblems():
    return loadNProblems(10**10)

"""
Same as above, but only load some small number of problems. Will load all problems if n exceeds total number.
"""
def loadNProblems(n):
    count = 0
    root_dir = '.'
    print("Loading all problems...")
    problems = []
    for directory, subdirectories, files in os.walk(root_dir):
        for filed in files:
            name = os.path.join(directory, filed)
            test_dir = ".\\texts"
            if name.startswith(test_dir) and name.endswith(".html"):
                refined_name = name.replace("\\", "/")
                try:
                    problems.append(problem.Problem(refined_name))
                except:
                    print("problem {} had a formatting issue:  {}".format(count, name))
                count += 1
                """Progress counter"""
                print("problem {} loaded:  {}".format(count, name))
                if count >= n:
                    return problems
    return problems

"""
Given a csv file path, returns a list of lists with each inner list corrresponding to a csv file line, a single
problem. The header line is ignored. The inner list contains raw strings from the csv.
"""
def loadAllProblemsFromCSV(path):
    lines = []
    with open(path, 'r') as file:
        for line in file.readlines():
            lines.append(line.split(","))
    return lines[1:]

"""Replace all non-alpha chars with spaces"""
def removeNumbers(str):
     return ''.join([i if i.isalpha() else ' ' for i in str])

"""Takes a list of features, in a list of lists, as read from a csv
Extracts out the text fields including input, output, main text, and title, and writes them to hardcoded file name."""
def writeWordFields(csv_list):
    important = [1,3,5,8]
    full_str = ""
    for fields in csv_list:
        for field_i in important:
            san = removeNumbers(fields[field_i])
            san = " ".join(san.split())
            full_str += san + " "
        full_str += "\n"
    with open("wordsOnly.txt", 'w') as file:
        file.write(full_str)

"""Will output a separate entry for each tag,problem pair"""
def writeWordFieldsAndTagsOnePerTagPerProblem(csv_list):
    important = [8, 3, 5, 1]
    tag_index = 6
    full_str = ""

    for fields in csv_list:

        text_str = ""
        for field_i in important:
            san = removeNumbers(fields[field_i])
            san = " ".join(san.split())
            text_str += san + " "


        raw = fields[tag_index]
        raw = ''.join([i if i.isalnum() or i == '-' or i == '/' else '' for i in raw])
        tags = raw.split("/")

        for tag in tags:
            if len(tag) == 0:
                continue
            full_str += text_str.strip() + "," + tag + "\n"

    with open("words_all_one_entry_per_tag_per_problem.csv", 'w') as file:
        file.write(full_str)

def writeWordFieldsAndAllTagsForProblem(csv_list):

    important = [8, 3, 5, 1]
    tag_index = 6
    full_str = ""

    for fields in csv_list:

        text_str = ""
        for field_i in important:
            san = removeNumbers(fields[field_i])
            san = " ".join(san.split())
            text_str += san + " "

        raw = fields[tag_index]
        raw = ''.join([i if i.isalnum() or i == '-' or i == '/' else '' for i in raw])
        tags = raw.split("/")

        full_str += text_str.strip() + "," + raw +  "\n"

    with open("words_all_with_tags_one_entry_per_problem.csv", 'w') as file:
        file.write(full_str)

"""Include a line for each problem tag pair, but also include a list of all acceptable tags for the problem."""
def writeWordFieldsWithAllTags(csv_list):
    important = [8, 3, 5, 1]
    tag_index = 6
    full_str = "main_text,tag,all_tags\n"

    for fields in csv_list:

        text_str = ""
        for field_i in important:
            san = removeNumbers(fields[field_i])
            san = " ".join(san.split())
            text_str += san + " "

        raw = fields[tag_index]
        raw = ''.join([i if i.isalnum() or i == '-' or i == '/' else '' for i in raw])
        tags = raw.split("/")

        for tag in tags:
            if len(tag) == 0:
                continue
            full_str += text_str.strip() + "," + tag + "," + raw + "\n"

    with open("words_all.csv", 'w') as file:
        file.write(full_str)

"""Addition of some custom group tags that are assigned to a problem that contains any one of multiple representative 
tags. The purpose is to try and make tags with more balanced YES/NO proportions.
 (something that is a 90%/10% split is not as helpful as 60%/40%)"""
def writeWordFieldsWithTagGroups(csv_list):
    all_graphs = ['dfsandsimilar', 'graphs', 'trees', 'shortestpaths', 'flows', 'graphmatchings']
    all_math = ['math', 'numbertheory', 'combinatorics', 'geometry', 'probabilities', 'matrices', 'fft']
    easy = ['implementation', 'bruteforce']
    all_strings = ['strings', 'stringsuffixstructures', 'expressionparsing']
    custom_tags_lists = [all_graphs, all_math, easy, all_strings]
    custom_tags = ['all_graphs', 'all_math', 'easy', 'all_strings']

    important = [8, 3, 5, 1]
    tag_index = 6
    full_str = "main_text,tags\n"

    for fields in csv_list:

        text_str = ""
        for field_i in important:
            san = removeNumbers(fields[field_i])
            san = " ".join(san.split())
            if field_i == 8:
                text_str += san*3 + " "
            else:
                text_str += san + " "


        raw = fields[tag_index]
        raw = ''.join([i if i.isalnum() or i == '-' or i == '/' else '' for i in raw])
        tags = raw.split("/")
        #no tags
        if len(tags) == 1 and len(tags[0]) == 0:
            continue

        for i in range(len(custom_tags_lists)):
            custom_list = custom_tags_lists[i]
            custom_tag = custom_tags[i]
            good = False
            for check in custom_list:
                if check in tags:
                    good = True
                    break
            if good:
                tags.append(custom_tag)

        tag_string = '[' + '/'.join(tags) + ']'
        full_str += text_str.strip() + "," + tag_string + "\n"

    with open("words_all_no_repeats.csv", 'w') as file:
        file.write(full_str)

#Outputs sorted list of tag frequencies to file
#Later could create conditional probs and output them too.
def writeTagFrequencies(csv_list):
    tag_index = 6
    num_problems_with_tags = 0

    counts = Counter()
    for problem in csv_list:
        raw = problem[tag_index]
        raw = ''.join([i if i.isalnum() or i == '-' or i == '/' else '' for i in raw])
        tags = raw.split("/")

        if len(raw) == 0: #Don't count problems that don't have any tags.
            continue
        num_problems_with_tags += 1
        for tag in tags:
            counts[tag] += 1
    tups = []

    for k,v in counts.items():
        tups.append((v,k,v/num_problems_with_tags))
    tups = reversed(sorted(tups))

    with open("tag_frequencies.txt", 'w') as file:
        for tup in tups:
            file.write(str(tup) + "\n")

#Outputs sorted list of tag frequencies to file. This one assumes the condensed csv form
def writeTagFrequenciesFromCondensedCSV(csv_list):
    tag_index = 1
    num_problems_with_tags = 0

    counts = Counter()
    for problem in csv_list:
        raw = problem[tag_index]
        raw = ''.join([i if i.isalnum() or i == '-' or i == '/' else '' for i in raw])
        tags = raw.split("/")

        if len(raw) == 0: #Don't count problems that don't have any tags.
            continue
        num_problems_with_tags += 1
        for tag in tags:
            counts[tag] += 1
    tups = []

    for k,v in counts.items():
        tups.append((v,k,v/num_problems_with_tags))
    tups = reversed(sorted(tups))

    with open("tag_frequencies.txt", 'w') as file:
        for tup in tups:
            file.write(str(tup) + "\n")

"""Return a Counter of tag -> frequency"""
def getTagFrequenciesFromCondensedCSV(csv_list):
    tag_index = 1
    num_problems_with_tags = 0

    counts = Counter()
    for problem in csv_list:
        raw = problem[tag_index]
        raw = ''.join([i if i.isalnum() or i == '-' or i == '/' else '' for i in raw])
        tags = raw.split("/")

        if len(raw) == 0: #Don't count problems that don't have any tags.
            continue
        num_problems_with_tags += 1
        for tag in tags:
            counts[tag] += 1

    for k,v in counts.items():
        counts[k] /= num_problems_with_tags
    return counts
"""
A main that acts as a sandbox for the above functions.
"""
if __name__ == '__main__':
    """
    import time
    start_time = time.clock()

    problems = loadAllProblems()
    print("{} problems loaded".format(len(problems)))

    for i in range(5):
        sam = random.choice(problems)
        print(sam)

    outputCSV(problems, "output_all.csv")

    print(time.clock() - start_time, "seconds")
    """

    #csvLines = loadAllProblemsFromCSV("output_all.csv")
    csvLines = loadAllProblemsFromCSV("words_all_no_repeats.csv")
    writeTagFrequencies(csvLines)
    #writeWordFieldsWithTagGroups(csvLines)


