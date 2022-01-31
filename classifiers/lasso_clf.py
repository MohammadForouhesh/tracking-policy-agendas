from sklearn.linear_model import SGDClassifier
from classifiers.meta_clf import MetaClf


class LassoClf(MetaClf):
    def __init__(self, **kwargs):
        super().__init__(classifier_instance=SGDClassifier(loss='modified_huber', penalty='l1'), **kwargs)