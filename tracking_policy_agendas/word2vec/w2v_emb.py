"""
Word2Vec Embedding

....................................................................................................
MIT License
Copyright (c) 2021-2023 AUT Iran, Mohammad H Forouhesh
Copyright (c) 2021-2022 MetoData.ai, Mohammad H Forouhesh
....................................................................................................
This module encapsulate the Word2Vec embedding of a given corpus.
"""

import pickle
import gensim
import numpy as np
import pandas as pd
from typing import List, Generator

from gensim import utils
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from .w2v_corpus import W2VCorpus


class W2VEmb:
    def __init__(self, text_document=None):
        self.wv2_corpus = None
        self.w2v_model = None
        self.tf_idf_transformation = None
        if text_document is not None: self.__init(text_document)

    def __init(self, text_document: pd.Series) -> None:
        """
        Constructor
        :param text_document:  text corpus
        :return:               None
        """
        text_document = text_document.fillna('')
        self.tf_idf_transformation = self.tf_idf_transformer(text_document)
        self.wv2_corpus = W2VCorpus(text_document)
        self.w2v_model = gensim.models.Word2Vec(sentences=self.wv2_corpus, min_count=1, vector_size=900, epochs=50)

    def __getitem__(self, text: str) -> np.ndarray:
        """
        getitem overwrite to get word embedding for a given text.
        :param text:    Input text.
        :return:        A numpy array of embedding array.
        """
        try:    return self.w2v_model.wv[text]
        except: return np.array([0 for _ in range(0, self.w2v_model.vector_size)])

    def tf_idf_transformer(self, text_series):
        """
        TF-IDF transformer for weighting words
        :param text_series:
        :return:
        """
        tfidf = Pipeline([('count', CountVectorizer(encoding='utf-8', min_df=3, #max_df=0.9,
                                                    max_features=900,
                                                    ngram_range=(1, 2))),
                          ('tfid', TfidfTransformer(sublinear_tf=True, norm='l2'))]).fit(text_series.ravel())
        return tfidf

    def encode(self, text: str) -> np.ndarray:
        """
        Encoding function
        :param text:    Input text
        :return:        A numpy array of embedding array.
        """
        stream = utils.simple_preprocess(text)
        tf_idf_vec = self.tf_idf_transformation.transform(stream).toarray()
        w2v_encode = self[stream]
        return np.mean(list(self.tf_idf_mean(tf_idf_vec, w2v_encode)), axis=0)

    def save(self, path: str) -> None:
        """
        A tool to save model w2v to disk
        :param path:   Saving path.
        :return:       None.
        """

        with open(path, 'wb') as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, path: str) -> None:
        """
        A tool to load w2v model from disk.
        :param path:   Model path.
        :return:       None
        """

        with open(path, 'rb') as f:
            self.__dict__.update(pickle.load(f).__dict__)

    @staticmethod
    def tf_idf_mean(tf_idf_vec: np.ndarray, w2v_encode: np.ndarray) -> Generator[List[float], None, None]:
        """
        Mean pooling to encode sentences using tf-idf weights of words.
        :param tf_idf_vec:  A tf-idf vector of the sentence
        :param w2v_encode:  A word2vec vector of the sentence
        :return:            A generator that yield relative vector of a word with respect to its tf-idf vector.
        """

        for ind in range(len(tf_idf_vec)):
            yield tf_idf_vec[ind]*w2v_encode[ind]
