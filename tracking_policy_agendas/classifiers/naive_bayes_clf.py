from sklearn.naive_bayes import GaussianNB
from .meta_sklearn_clf import MetaSkLearnClf


class GNBClf(MetaSkLearnClf):
    def __init__(self, **kwargs):
        super().__init__(classifier_instance=GaussianNB(), **kwargs)
