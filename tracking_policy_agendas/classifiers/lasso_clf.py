from sklearn.linear_model import SGDClassifier
from .meta_sklearn_clf import MetaSkLearnClf


class LassoClf(MetaSkLearnClf):
    def __init__(self, **kwargs):
        super().__init__(classifier_instance=SGDClassifier(loss='modified_huber', penalty='l1'), **kwargs)
