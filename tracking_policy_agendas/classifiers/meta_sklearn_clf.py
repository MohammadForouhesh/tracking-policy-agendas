"""
Abstract class for SKLearn Classifiers

....................................................................................................
MIT License
Copyright (c) 2021-2023 AUT Iran, Mohammad H Forouhesh
Copyright (c) 2021-2022 MetoData.ai, Mohammad H Forouhesh
....................................................................................................
This module abstracts sklearn classifier.
"""

import os
import pickle
from .meta_clf import MetaClf


class MetaSkLearnClf(MetaClf):
    def __init__(self, classifier_instance, **kwargs):
        super().__init__(classifier_instance=classifier_instance, **kwargs)
        if kwargs['load_path'] is not None: self.load_model(kwargs['load_path'])

    def load_model(self, load_path: str):
        """
        A tool to load model from disk.
        :param load_path:   Model path.
        :return:            None
        """

        loading_prep = lambda string: f'model_dir/{load_path}/{string}'
        self.emb.load(loading_prep('emb.pkl'))
        with open(loading_prep('model.pkl'), 'rb') as f:
            self.clf = pickle.load(f)
        with open(loading_prep('scaler.pkl'), 'rb') as f:
            self.scaler = pickle.load(f)

    def save_model(self, save_path: str):
        """
        A tool to save model to disk
        :param save_path:   Saving path.
        :return:            None.
        """

        os.makedirs(f'model_dir/{save_path}', exist_ok=True)
        saving_prep = lambda string: f'model_dir/{save_path}/{string}'
        self.emb.save(saving_prep('emb.pkl'))
        with open(saving_prep('scaler.pkl'), 'wb') as f:
            pickle.dump(self.scaler, f, pickle.HIGHEST_PROTOCOL)
        with open(saving_prep('model.pkl'), 'wb') as f:
            pickle.dump(self.clf, f, pickle.HIGHEST_PROTOCOL)
