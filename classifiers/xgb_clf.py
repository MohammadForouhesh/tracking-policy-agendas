from xgboost import XGBClassifier
from classifiers.meta_clf import MetaClf


class XgbClf(MetaClf):
    def __init__(self, **kwargs):
        super().__init__(classifier_instance=XGBClassifier(n_estimators=300), **kwargs)

    def inference(self, input_text: str):
        vector = self.scaler.transform(self.emb.encode(input_text).reshape(1, -1))
        return self.clf.predict(vector)[0]

    def inference_proba(self, input_text: str):
        vector = self.scaler.transform(self.emb.encode(input_text).reshape(1, -1))
        return 1 if self.clf.predict_proba(vector)[0][1] >= 0.70 else 0

    def predict_proba(self, array):
        return list(map(int, self.clf.predict_proba(array)[:, 1] >= 0.70))