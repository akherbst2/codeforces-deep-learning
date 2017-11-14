from bs4 import BeautifulSoup
import util

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

        path_items = path.split("/")
        self.contest = path_items[1]
        self.letter = path_items[2].split(".")[0]
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

        #Later, may want to add sample tests, and Notes to this class, but it is difficult to parse the samples
        # in a useful fashion.
        #self.sample_tests = page_soup.find(attrs={'class': "sample-test"}).findAll
        #print(self.sample_tests)


    def parse_pickle(self, path):
        pass
        #later, maybe load pickle and create object that way

    def __str__(self):
        return util.stringify(self)

if __name__ == '__main__':
    #basic test. Load a single file. No tags
    problem = Problem("texts/889/E.html")
    print(problem)

    #single problem with multiple tags
    problem = Problem("texts/888/G.html")
    print(problem)

    #single problem with multiple tags
    problem = Problem("./texts/888/G.html")
    print(problem)