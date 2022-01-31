import pickle
import gensim
import numpy as np
import pandas as pd
from word2vec.w2v_corpus import W2VCorpus


class W2VEmb:
    def __init__(self, text_series=None):
        self.wv2_corpus = None
        self.w2v_model = None
        if text_series is not None: self.__init(text_series)

    def __init(self, text_series: pd.Series):
        text_series = text_series.fillna('')
        self.wv2_corpus = W2VCorpus(text_series)
        self.w2v_model = gensim.models.Word2Vec(sentences=self.wv2_corpus)

    def __getitem__(self, text: str) -> np.ndarray:
        return self.w2v_model.wv([text])

    def encode(self, text: str) -> np.ndarray:
        return self[text]

    def save(self, path: str):
        with open(path, 'wb') as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, path: str):
        with open(path, 'rb') as f:
            self.__dict__.update(pickle.load(f).__dict__)