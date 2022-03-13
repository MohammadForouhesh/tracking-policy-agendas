"""
Lasso Classifier

....................................................................................................
MIT License
Copyright (c) 2021-2023 AUT Iran, Mohammad H Forouhesh
Copyright (c) 2021-2022 MetoData.ai, Mohammad H Forouhesh
....................................................................................................
This module encapsulate the Lasso classifier.
"""

from sklearn.linear_model import SGDClassifier
from .meta_sklearn_clf import MetaSkLearnClf


class LassoClf(MetaSkLearnClf):
    def __init__(self, **kwargs):
        super().__init__(classifier_instance=SGDClassifier(loss='modified_huber', penalty='l1'), **kwargs)
