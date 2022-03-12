from sklearn.linear_model import PassiveAggressiveClassifier
from .meta_clf import MetaClf


class PAClf(MetaClf):
    def __init__(self, **kwargs):
        super().__init__(classifier_instance=PassiveAggressiveClassifier(max_iter=1000, loss='squared_hinge'), **kwargs)
