from sklearn.feature_extraction.text import TfidfTransformer

transformer = TfidfTransformer(smooth_idf=False)

"""
Computes a tf-idf score matrix for every word in a problem title, main-text,
input specification, and output specification

input: ("wordsOnly.txt") the name of the file containing all the text of every problem,
separated by a new line character.

output: a scipy sparse matrix containing an nxd matrix of tfidf word scores
for a particular word in a particular problem
n = # problems
d = # unique words in all problems
"""
def get_tfidf_scores(input_file):
    bag_of_words = set()
    with open(input_file) as file:
        for line in file.readlines():
            for word in line.split(' '):
                bag_of_words.add(word)

    bag_of_words = list(sorted(bag_of_words))
    index_of = {word: idx for idx, word in enumerate(bag_of_words)}
    counts = []
    with open(input_file) as file:
        for line in file.readlines():
            word_count = [0] * len(bag_of_words)
            for word in line.split(' '):
                word_idx = index_of[word]
                word_count[word_idx] += 1
            counts.append(word_count)

    tfidf = transformer.fit_transform(counts)
    return tfidf

"""
Input file should be a csv file path.
First line of csv is headers, which will be ignored.

Returns a set of feature vectors, an array of labels for training, and an array of acceptable guesses for training
"""
def get_tfidf_scores_and_labels_from_csv(input_file):
    bag_of_words = set()
    line_num = 0
    x_lines = []
    y_lines = []
    z_lines = []

    with open(input_file) as file:
        for line in file.readlines():
            line = line.strip()
            if line_num != 0:
                x,y,z = line.split(',')
                for word in x.split(' '):
                    bag_of_words.add(word)

                z = z.split("/")
                x_lines.append(x)
                y_lines.append(y)
                z_lines.append(z)
            line_num += 1

    bag_of_words = list(sorted(bag_of_words))
    index_of = {word: idx for idx, word in enumerate(bag_of_words)}
    counts = []

    for x in x_lines:
        word_count = [0] * len(bag_of_words)
        for word in x.split(' '):
            word_idx = index_of[word]
            word_count[word_idx] += 1
        counts.append(word_count)

    tfidf = transformer.fit_transform(counts)
    return tfidf, y_lines, z_lines
