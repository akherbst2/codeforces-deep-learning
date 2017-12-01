
import os
import problem
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
CSV fields will simply have strings of the format given by str(field)"""

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



if __name__ == '__main__':
    import time
    start_time = time.clock()

    problems = loadAllProblems()
    print("{} problems loaded".format(len(problems)))

    for i in range(5):
        sam = random.choice(problems)
        print(sam)

    outputCSV(problems, "output_all.csv")

    print(time.clock() - start_time, "seconds")
