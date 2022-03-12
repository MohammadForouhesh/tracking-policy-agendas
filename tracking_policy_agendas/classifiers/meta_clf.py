import os
import pickle
import pandas as pd
from tqdm import tqdm
from ..word2vec.w2v_emb import W2VEmb
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


class MetaClf:
    def __init__(self, classifier_instance, text_array: list = None, embedding_doc: list = None, labels: list = None, load_path: str = None):
        if not isinstance(text_array, pd.Series): text_array = pd.Series(text_array)

        self.clf = classifier_instance
        self.emb = W2VEmb()
        self.scaler = None
        if load_path is not None: self.load_model(load_path)
        else:
            assert text_array is not None and labels is not None
            text_array.fillna('', inplace=True)
            self.emb = W2VEmb(embedding_doc)

            encoded = list(map(self.emb.encode, tqdm(text_array)))
            self.labels = list(labels)
            self.scaler = self.prep_scaler(encoded)
            self.encoded_input = self.scaler.transform(encoded)

    def prep_scaler(self, encoded):
        scaler = MinMaxScaler()
        scaler.fit(encoded)
        return scaler

    def fit(self):
        X_train, X_test, y_train, y_test = train_test_split(self.encoded_input, self.labels, test_size=0.2,
                                                            random_state=42, stratify=self.labels)
        self.clf.fit(X_train, y_train)
        print('score: ', self.clf.score(X_test, y_test))
        print('============================trian============================')
        print(classification_report(y_train, self.clf.predict(X_train)))
        print('=============================test============================')
        print(classification_report(y_test, self.clf.predict(X_test)))
        return self.clf

    def load_model(self, load_path: str):
        loading_prep = lambda string: f'model_dir/{load_path}/{string}'
        self.clf.load_model(loading_prep('model.json'))
        self.emb.load(loading_prep('emb.pkl'))
        with open(loading_prep('scaler.pkl'), 'rb') as f:
            self.scaler = pickle.load(f)

    def save_model(self, save_path: str):
        os.makedirs(f'model_dir/{save_path}', exist_ok=True)
        saving_prep = lambda string: f'model_dir/{save_path}/{string}'
        self.clf.save_model(saving_prep('model.json'))
        self.emb.save(saving_prep('emb.pkl'))
        with open(saving_prep('scaler.pkl'), 'wb') as f:
            pickle.dump(self.scaler, f, pickle.HIGHEST_PROTOCOL)

    def predict(self, input_text: str):
        vector = self.scaler.transform(self.emb.encode(input_text).reshape(1, -1))
        return self.clf.predict(vector)[0]
