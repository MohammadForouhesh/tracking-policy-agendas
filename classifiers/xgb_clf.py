import os
import pickle
import pandas as pd
from tqdm import tqdm
from xgboost import XGBClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


class XgbClf():
    def __init__(self, text_array: list = None, labels: list = None, load_path: str = None):
        if not isinstance(text_array, pd.Series): text_array = pd.Series(text_array)

        self.xgb = XGBClassifier(n_estimators=300)
        self.emb = HandCraftEmbedding()
        self.scaler = None
        if load_path is not None: self.load_model(load_path)
        else:
            assert text_array is not None and labels is not None
            text_array.fillna('', inplace=True)
            self.emb = HandCraftEmbedding(text_array)

            encoded = list(map(self.emb.encode, tqdm(text_array)))
            self.labels = list(labels)
            self.scaler = self.prep_scaler(encoded)
            self.encoded_input = self.scaler.transform(encoded)

    def prep_scaler(self, encoded):
        scaler = MinMaxScaler()
        scaler.fit(encoded)
        return scaler

    def build(self):
        X_train, X_test, y_train, y_test = train_test_split(self.encoded_input, self.labels, test_size=0.2,
                                                            random_state=42, stratify=self.labels)
        self.xgb.fit(X_train, y_train)
        self.xgb.score(X_test, y_test)
        print('============================trian============================')
        print(classification_report(y_train, self.xgb.predict(X_train)))
        print('=============================test============================')
        print(classification_report(y_test, self.xgb.predict(X_test)))
        print('=========================proba=test==========================')
        print(classification_report(y_test, self.predict_proba(X_test)))
        return self.xgb

    def load_model(self, load_path: str):
        loading_prep = lambda string: f'model_dir/{load_path}/{string}'
        self.xgb.load_model(loading_prep('model.json'))
        self.emb.load(loading_prep('emb.pkl'))
        with open(loading_prep('scaler.pkl'), 'rb') as f:
            self.scaler = pickle.load(f)

    def save_model(self, save_path: str):
        os.makedirs(f'model_dir/{save_path}', exist_ok=True)
        saving_prep = lambda string: f'model_dir/{save_path}/{string}'
        self.xgb.save_model(saving_prep('model.json'))
        self.emb.save(saving_prep('emb.pkl'))
        with open(saving_prep('scaler.pkl'), 'wb') as f:
            pickle.dump(self.scaler, f, pickle.HIGHEST_PROTOCOL)

    def inference(self, input_text: str):
        vector = self.scaler.transform(self.emb.encode(input_text).reshape(1, -1))
        return self.xgb.predict(vector)[0]

    def inference_proba(self, input_text: str):
        vector = self.scaler.transform(self.emb.encode(input_text).reshape(1, -1))
        return 1 if self.xgb.predict_proba(vector)[0][1] >= 0.70 else 0

    def predict_proba(self, array):
        return list(map(int, self.xgb.predict_proba(array)[:, 1] >= 0.70))