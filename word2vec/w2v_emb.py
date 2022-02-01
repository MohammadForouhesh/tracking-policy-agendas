import pickle
import gensim
import numpy as np
import pandas as pd
from gensim import utils
from sklearn.pipeline import Pipeline
from word2vec.w2v_corpus import W2VCorpus
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


class W2VEmb:
    def __init__(self, text_document=None):
        self.wv2_corpus = None
        self.w2v_model = None
        self.tf_idf_transformation = None
        if text_document is not None: self.__init(text_document)

    def __init(self, text_document: pd.Series):
        text_document = text_document.fillna('')
        self.tf_idf_transformation = self.tf_idf_transformer(text_document)
        self.wv2_corpus = W2VCorpus(text_document)
        self.w2v_model = gensim.models.Word2Vec(sentences=self.wv2_corpus, min_count=1,
                                                vector_size=300, sg=1, epochs=20)

    def __getitem__(self, text: str) -> np.ndarray:
        try:    return self.w2v_model.wv[text]
        except: return np.array([0 for _ in range(0, self.w2v_model.vector_size)])

    def tf_idf_transformer(self, text_series):
        tfidf = Pipeline([('count', CountVectorizer(encoding='utf-8', #min_df=0.01, max_df=0.9,
                                                    max_features=300,
                                                    ngram_range=(1, 2))),
                          ('tfid', TfidfTransformer(sublinear_tf=True, norm='l2'))]).fit(text_series.ravel())
        return tfidf

    def encode(self, text: str) -> np.ndarray:
        stream = utils.simple_preprocess(text)
        tf_idf_vec = self.tf_idf_transformation.transform(stream).toarray()
        w2v_encode = self[stream]
        return np.mean(list(self.tf_idf_mean(tf_idf_vec, w2v_encode)), axis=0)

    def save(self, path: str):
        with open(path, 'wb') as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, path: str):
        with open(path, 'rb') as f:
            self.__dict__.update(pickle.load(f).__dict__)

    @staticmethod
    def tf_idf_mean(tf_idf_vec: np.ndarray, w2v_encode: np.ndarray):
        for ind in range(len(tf_idf_vec)):
            yield tf_idf_vec[ind]*w2v_encode[ind]
