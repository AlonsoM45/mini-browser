""" STEP 0:  Import dependencies """
from __future__ import absolute_import, division, print_function
import codecs # for encoding
import glob # regex
import multiprocessing # concurrency
import os # OS, reading files
import  pprint # pretty prinying
import re # regular expression
import nltk # natural language toolkit
import gensim.models.word2vec as w2v # word 2 vec
import sklearn.manifold # dimensionalitu reduction
import numpy as np # math
import matplotlib.pyplot as plt # plotting
import pandas as pd # parse pandas
import seaborn as sns # visualization

""" STEP 1:  Process our data """
# clean data
#nltk.download('punkt') # pretrained tokenizer
#nltk.download('stopwords') # words like: and, the, an, a, of ...

# load all in a variable
path = "C:\\Users\\Lenovo\\Desktop\\DataSet\\word_vectors_game_of_thrones-LIVE-master\\data\\*.txt"

book_filenames = sorted(glob.glob(path))
print(book_filenames)

corpus_raw = ""
for book_filename in book_filenames:
    print("Reading '{0}'...".format(book_filename))
    with codecs.open(book_filename, "r", "utf-8") as book_file:
        corpus_raw += book_file.read()
    print("Corpus is now {0} characters long".format(len(corpus_raw)))
    print()

# Split the corpus into sentences
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
raw_sentences = tokenizer.tokenize(corpus_raw)

def sentence_to_wordlist(raw):
    """
    Convert into a list of words, remove unnecessary, split
    into words, no hyphens list of words
    """
    clean = re.sub("[^a-zA-Z]", " ", raw)
    words = clean.split()
    return words

# sentence where each word is tokenized
senteces = []
for raw_sentence in raw_sentences:
    if (len(raw_sentence) > 0):
        senteces.append(sentence_to_wordlist(raw_sentence))

print(raw_sentences[5], type(raw_sentences[5]))
print(sentence_to_wordlist(raw_sentences[5]))

token_count = sum([len(sentece) for sentece in senteces])
print("The book corpus contains {0:,} tokens".format(token_count))

""" Train Word2Vec
ONCE we have vectors, 3 main tasks that vectors help with:
    1- DISTANCE
    2- SIMILARITY
    3- RANKING
"""

# Dimensionality of the resulting word vectors.
"""
More dimensions, more computationally expensive to train,
but more acurate.
More dimensions = more generalized
"""
num_features = 300

# Minimun word count threshold
min_word_count = 3

# Number of threads to run in parallel, more workers, fastest we train
num_workers = multiprocessing.cpu_count()

# Context window length
context_size = 7

# Downsample setting for frequent words: 0 - 1e-5 is good for this
downsampling = 1e-3

# Seed for the RNG, to make the results reproducible: deterministic
seed = 1

thrones2vec = w2v.Word2Vec(
    sg=1,
    seed=seed,
    workers=num_workers,
    size=num_features,
    min_count=min_word_count,
    window=context_size,
    sample=downsampling
)
thrones2vec.build_vocab(senteces)
#print("Word2Vec vocaubulary length:", len(thrones2vec.vocab))

""" Start the training """
thrones2vec.train(senteces)