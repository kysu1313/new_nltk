from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer
import nltk


example_text = "Hello there, how are you? Beautiful day today isn't it. You should buy Google stock, its low."

stop_words = set(stopwords.words("english"))
words = word_tokenize(example_text)
tokenized_sentence = sent_tokenize(example_text)

# One-line for-loop
filtered_sentence = [w for w in words if not w in stop_words]

# print(filtered_sentence)

ps = PorterStemmer()
example_words = ["python","pythoning","pythoner","pythonly","pythoned"]

for w in example_words:
    print(ps.stem(w))

# for wo in words:
#     print(ps.stem(wo))
def get_words_from_file(file):
    try:
        f = open(file, "r")
        f_words = [word.split(" ") for word in f.readlines()]
        f.close()
        return f_words
    except Exception:
        print("no file")

def get_filtered_words(text):
    filt_words = []
    for line in text:
        for w in line:
            if w not in stop_words:
                filt_words.append(w)
    return filt_words

def get_unfiltered_words(text):
    un_filt_words = []
    for line in file_words:
        for w in line:
            un_filt_words.append(w)
    return un_filt_words

file_words = get_words_from_file("/Users/kylesupple/Desktop/Programming/nltk_code/proj_2_nltk/warAndPeace_copy.txt")

print("\nfiltered: " + str(len(get_filtered_words(file_words))))
print("unfiltered: " + str(len(get_unfiltered_words(file_words))))

#punkt example
train_txt = state_union.raw("2005-GWBush.txt")
sample_txt = state_union.raw("2006-GWBush.txt")
custom_sample_txt = PunktSentenceTokenizer(train_txt)

tokenized = custom_sample_txt.tokenize(sample_txt)

def process_content(txt):
    tag_words = []
    for i in txt[5:]:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        tag_words.append(tagged)

        namedEnt = nltk.ne_chunk(tagged)
        namedEnt.draw()
        
    #     #chunk words using regex expressions
    #     chunkGram = r"""Chunk: {<.*>+}
    #                             }<VB.?|IN|DT>+{"""
    #     # chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
    #     chunkParser = nltk.RegexpParser(chunkGram)
    #     chunked = chunkParser.parse(tagged)

    #     chunked.draw()

    # return tag_words
    
tagged_speech_words = process_content(tokenized)

# for items in tagged_speech_words:
#     for var, name in items:
#         if name == 'NNP':
#             print(var)

# for items in tagged_speech_words:
#     if len(items) >= 2:
#         if atb == 'RB':
#             print(var)
