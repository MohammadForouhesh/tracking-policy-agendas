"""
Naive Bayes Classifier

....................................................................................................
MIT License
Copyright (c) 2021-2023 AUT Iran, Mohammad H Forouhesh
Copyright (c) 2021-2022 MetoData.ai, Mohammad H Forouhesh
....................................................................................................
This module encapsulate the Naive Bayes classifier.
"""

from sklearn.naive_bayes import GaussianNB
from .meta_sklearn_clf import MetaSkLearnClf


class GNBClf(MetaSkLearnClf):
    def __init__(self, **kwargs):
        super().__init__(classifier_instance=GaussianNB(), **kwargs)
