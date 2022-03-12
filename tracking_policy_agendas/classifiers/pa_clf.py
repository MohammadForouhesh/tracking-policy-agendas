from sklearn.linear_model import PassiveAggressiveClassifier
from .meta_sklearn_clf import MetaSkLearnClf


class PAClf(MetaSkLearnClf):
    def __init__(self, **kwargs):
        super().__init__(classifier_instance=PassiveAggressiveClassifier(max_iter=1000, loss='squared_hinge'), **kwargs)
