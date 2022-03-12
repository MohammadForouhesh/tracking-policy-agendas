from sklearn.naive_bayes import GaussianNB
from meta_clf import MetaClf


class GNBClf(MetaClf):
    def __init__(self, **kwargs):
        super().__init__(classifier_instance=GaussianNB(), **kwargs)
