#Canabalized from https://stackoverflow.com/questions/32910096/is-there-a-way-to-auto-generate-a-str-implementation-in-python
import os
import problem
import random

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

"""
Return list of Problem class objects. Roughly 4000
"""
def loadAllProblems():
    root_dir = '.'
    print("Loading all problems...")
    problems = []
    for directory, subdirectories, files in os.walk(root_dir):
        for filed in files:
            name = os.path.join(directory, filed)
            test_dir = ".\\texts"
            if name.startswith(test_dir) and name.endswith(".html"):
                refined_name = name.replace("\\", "/")
                problems.append(problem.Problem(refined_name))
    return problems

if __name__ == '__main__':
    import time
    start_time = time.clock()

    problems = loadAllProblems()
    print("{} problems loaded".format(len(problems)))
    for i in range(5):
        sam = random.choice(problems)
        print(sam)
    print(time.clock() - start_time, "seconds")
