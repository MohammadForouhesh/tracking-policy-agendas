from xgboost import XGBClassifier
from .meta_clf import MetaClf


class XgbClf(MetaClf):
    def __init__(self, **kwargs):
        super().__init__(classifier_instance=XGBClassifier(n_estimators=300), **kwargs)
