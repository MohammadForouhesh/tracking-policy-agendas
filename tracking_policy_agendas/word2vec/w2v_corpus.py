"""
Word2Vec Corpus Building

....................................................................................................
MIT License
Copyright (c) 2021-2023 AUT Iran, Mohammad H Forouhesh
Copyright (c) 2021-2022 MetoData.ai, Mohammad H Forouhesh
....................................................................................................
This module contains the implementation of word2vec data generation.
"""

from gensim import utils


class W2VCorpus:
    def __init__(self, corpus):
        self.corpus = corpus

    def __iter__(self):
        for line in self.corpus:
            yield utils.simple_preprocess(line)
