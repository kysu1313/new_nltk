from nltk.corpus import wordnet


word1 = input("Enter a word: ")
word2 = input("Enter a word to compare it with: ")

input_word_1 = word1 + ".n.01"
input_word_2 = word2 + ".n.01"

#synset
syns = wordnet.synsets("program")
w1 = wordnet.synset(input_word_1)
w2 = wordnet.synset(input_word_2)

sim = w1.wup_similarity(w2) * 100
print(("A " + word1 + " is {:3.2f} percent similar to a " + word2).format(sim))
