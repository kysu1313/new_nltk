from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk


test_text = "Hello, my name is Kyle, what is yours? Do you like to eat glue too? I hear Amazon stock is about to go up, buy now!"

#tokenize by word
tokenized_words = word_tokenize(test_text)
#tokenize by sentence
tokenized_sentence = sent_tokenize(test_text)
#import stopwords
stop_words = set(stopwords.words("english"))

#function to import a text file
def get_words_from_file(file):
    try:
        f = open(file, "r")
        f_words = []
        for word in f.readlines():
            f_words.append(word.split(" "))
        f.close()
        return f_words
    except Exception:
        print("no file")

#return the words and their types
def categorize_text(text):
    txt = word_tokenize(text)
    tags = nltk.pos_tag(txt)
    return tags

#return text with stopwords removed
def get_filtered_words(text):
    filt_words = []
    for line in text:
        for w in line:
            if w not in stop_words:
                filt_words.append(w)
    return filt_words

#return plain text
def get_unfiltered_words(text):
    un_filt_words = []
    for line in file_words:
        for w in line:
            un_filt_words.append(w)
    return un_filt_words


file_words = get_words_from_file("/Users/kylesupple/Desktop/Programming/nltk_code/proj_2_nltk/warAndPeace_copy.txt")

print("Unfiltered: " + str(len(get_unfiltered_words(file_words))))
print("Filtered: " + str(len(get_filtered_words(file_words))))

