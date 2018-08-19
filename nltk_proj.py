import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# print(documents)

all_words = []

for w in movie_reviews.words():
    w = w.lower()
    all_words.append(w)

print(len(all_words))

all_words = nltk.FreqDist(all_words)

#print most common words, and print num of times "stupid" shows up
# print(all_words.most_common(15))
# print(all_words["fuck"])

word_features = list(all_words.keys())[:10000]

def find_features(doc):
    words = set(doc)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

# print(find_features(movie_reviews.words("neg/cv000_29416.txt")))

feature_sets = [(find_features(rev), category) for (rev, category) in documents]

training_set = feature_sets[:6000]
testing_set = feature_sets[6000:]

classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Naive Bayes Classifier accuracy: ", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)