import numpy as np
import tfidf
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import KFold

num_splits = 10

"""
Problem: This currently guesses implementation almost all the time. It is what I had feared.
See this paper for a possible solution.
https://www.cs.waikato.ac.nz/~eibe/pubs/FrankAndBouckaertPKDD06new.pdf
"""
def multinomial_naive_bayes_classifier():
    X,y,z = tfidf.get_tfidf_scores_and_labels_from_long_csv("words_all.csv")

    clf = MultinomialNB(alpha=0.1)

    kf = KFold(n_splits=num_splits)
    kf.get_n_splits(X)

    KFold(n_splits=num_splits, random_state=None, shuffle=True)

    fold_num = 0
    accuracies = []
    for train_index, test_index in kf.split(X):

        X_train, X_test = X[train_index], X[test_index]
        y_train = [y[index] for index in train_index]
        y_test = [y[index] for index in test_index]
        z_test = [z[index] for index in test_index]

        clf.fit(X_train, y_train)

        correct = 0
        incorrect = 0

        test_num = 0
        for x in X_test:
            guess = clf.predict(x)
            print(guess, z_test[test_num])
            if guess in z_test[test_num]:
                correct += 1
            else:
                incorrect += 1
            test_num += 1
        accuracy = correct / (correct + incorrect)
        accuracies.append(accuracy)
        print("Results for fold {}:  Accuracy = {}".format(fold_num, accuracy))
        fold_num += 1
    print("Average accuracy is {}".format(sum(accuracies) / float(len(accuracies))))

def bernoulli_naive_bayes_classifier():
    X, Y = tfidf.get_tfidf_scores_and_labels_from_short_csv("words_all_no_repeats.csv")

    all_tags = set()
    for y in Y:
        for tag in y:
            all_tags.add(tag)

    clf = BernoulliNB(alpha=.1)

    for tag in sorted(all_tags):
        if len(tag.strip()) == 0:
            continue
        print("Beginning cross validation for tag {}".format(tag))

        y = []
        for problem_tags in Y:
            if tag in problem_tags:
                y.append(1)
            else:
                y.append(0)

        kf = KFold(n_splits=num_splits)
        kf.get_n_splits(X)

        KFold(n_splits=num_splits, random_state=None, shuffle=True)

        fold_num = 0
        accuracies = []
        for train_index, test_index in kf.split(X):

            X_train, X_test = X[train_index], X[test_index]
            y_train = [y[index] for index in train_index]
            y_test = [y[index] for index in test_index]

            clf.fit(X_train, y_train)

            correct = 0
            incorrect = 0

            true_guess_count = 0
            false_guess_count = 0

            test_num = 0
            for x in X_test:
                guess = clf.predict(x)
                #print(guess)
                if guess == y_test[test_num]:
                    correct += 1
                else:
                    incorrect += 1
                if guess == 1:
                    true_guess_count += 1
                else:
                    false_guess_count += 1
                test_num += 1
            accuracy = correct / (correct + incorrect)
            accuracies.append(accuracy)
            print("Results for fold {} of tag {}:  Accuracy = {} ; true_guesses = {}; false_guesses = {}"
                  .format(fold_num, tag,  accuracy, true_guess_count, false_guess_count))

            fold_num += 1
        print("Average accuracy for tag {} is {}".format(tag, sum(accuracies) / float(len(accuracies))))

if __name__ == '__main__':
    #multinomial_naive_bayes_classifier()
    bernoulli_naive_bayes_classifier()

