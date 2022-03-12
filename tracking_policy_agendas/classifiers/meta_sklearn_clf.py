import os
import pickle
from .meta_clf import MetaClf


class MetaSkLearnClf(MetaClf):
    def __init__(self, classifier_instance, **kwargs):
        super().__init__(classifier_instance=classifier_instance, **kwargs)

    def load_model(self, load_path: str):
        loading_prep = lambda string: f'model_dir/{load_path}/{string}'
        self.emb.load(loading_prep('emb.pkl'))
        with open(loading_prep('model.pkl'), 'rb') as f:
            self.scaler = pickle.load(f)
        with open(loading_prep('scaler.pkl'), 'rb') as f:
            self.scaler = pickle.load(f)

    def save_model(self, save_path: str):
        os.makedirs(f'model_dir/{save_path}', exist_ok=True)
        saving_prep = lambda string: f'model_dir/{save_path}/{string}'
        self.emb.save(saving_prep('emb.pkl'))
        with open(saving_prep('scaler.pkl'), 'wb') as f:
            pickle.dump(self.scaler, f, pickle.HIGHEST_PROTOCOL)
        with open(saving_prep('model.pkl'), 'wb') as f:
            pickle.dump(self.clf, f, pickle.HIGHEST_PROTOCOL)
