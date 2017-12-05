import numpy as np
import tfidf
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold

num_splits = 10
def naive_bayes_classifier():
    X,y = tfidf.get_tfidf_scores_and_labels_from_csv("words_all.csv")
   
    clf = MultinomialNB()

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

        test_num = 0
        for x in X_test:
            guess = clf.predict(x)
            if guess == y[test_num]:
                correct += 1
            else:
                incorrect += 1
            test_num += 1
        accuracy = correct / (correct + incorrect)
        accuracies.append(accuracy)
        print("Results for fold {}:  Accuracy = {}".format(fold_num, accuracy))
        fold_num += 1
    print("Average accuracy is {}".format(sum(accuracies) / float(len(accuracies))))

if __name__ == '__main__':
    naive_bayes_classifier()

