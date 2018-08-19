from nltk.corpus import movie_reviews
from nltk.tokenize import sent_tokenize

'''
-To use sample text in the corpus file. 
-go to: /Users/kylesupple/nltk_data/corpora
-Then use: from nltk.corpus import name_of_file
-store the txt in a variable with: txt = name_of_file.raw("txt_file_name.txt")
-tokenize it with: tok = sent_tokenize(txt)
'''


sample = movie_reviews.raw("neg/cv000_29416.txt")
tok = sent_tokenize(sample)

print(tok[5:15])
