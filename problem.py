from bs4 import BeautifulSoup
import util


"""
Loads a single problem by giving a file path to an html file.
Involves parsing of html using beautiful soup

Note, input path must be of the form
"texts/<contest #>/<Problem Letter String>.html"

See bottom of file for examples.
"""

class Problem:
    def __init__(self, file_path):
        if file_path.endswith(".html"):
            self.parse_raw_html(file_path)
        elif file_path.endswith(".pkl"):
            self.parse_pickle(file_path)

    def parse_raw_html(self, path):
        raw_html = "EMPTY"
        with open(path, 'rb') as infile:
            raw_html = infile.read()

        page_soup = BeautifulSoup(raw_html, "lxml")

        #very sensitive to input format...
        path_items = path.split("/")
        self.contest = path_items[2]
        self.letter = path_items[3].split(".")[0]

        self.title = page_soup.find(attrs={'class': 'title'}).text
        self.time_limit = page_soup.find(
            attrs={'class': 'time-limit'}).text.split('time limit per test')[1]
        self.memory_limit = page_soup.find(
            attrs={'class': 'memory-limit'}).text.split('memory limit per test')[1]
        self.main_text = page_soup.find(
            attrs={'class': 'header'}).next_sibling.text
        self.input_specification = "Input".join(page_soup.find(
            attrs={'class': 'input-specification'}).text.split('Input')[1:])
        self.output_specification = "Output".join(page_soup.find(
            attrs={'class': 'output-specification'}).text.split('Output')[1:])

        tag_boxes = page_soup.findAll(attrs={'class': 'tag-box'})
        self.tags = []

        for tag_box in tag_boxes:
            self.tags.append(tag_box.text.strip())

        #Sanitize the fields

        self.contest = self.sanitize(self.contest)
        self.letter = self.sanitize(self.letter)
        self.title = self.sanitize(self.title)
        self.time_limit = self.sanitize(self.time_limit)
        self.memory_limit = self.sanitize(self.memory_limit)
        self.main_text = self.sanitize(self.main_text)
        self.input_specification = self.sanitize(self.input_specification)
        self.output_specification = self.sanitize(self.output_specification)
        for i in range(len(self.tags)):
            self.tags[i] = self.sanitize(self.tags[i])

        #Later, may want to add sample tests, and Notes to this class, but it is difficult to parse the samples
        # in a useful fashion.
        #self.sample_tests = page_soup.find(attrs={'class': "sample-test"}).findAll
        #print(self.sample_tests)

    """
    Currently, removes all chars to make it alpha-numeric with spaces and hyphens
    """
    def sanitize(self, string):
        #Remove unwanted chars
        raw =  ''.join([i if ord(i) < 128 and (i.isalnum() or i.isspace() or i == '-') else ' ' for i in string])

        #Condense extra whitespace
        return ' '.join(raw.split())

    def parse_pickle(self, path):
        pass
        #later, maybe load pickle and create object that way

    def __str__(self):
        return util.stringify(self)



if __name__ == '__main__':
    #basic test. Load a single file. No tags
    problem = Problem("./texts/889/E.html")
    print(problem)

    #single problem with multiple tags
    problem = Problem("./texts/888/G.html")
    print(problem)

    #Some problems with bad formats. All problems from comp 524 should be ignored
    #problem = Problem("./texts/524/A.html")

    problem = Problem("./texts/711/E.html")