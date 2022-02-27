from sklearn.linear_model import PassiveAggressiveClassifier
from classifiers.meta_clf import MetaClf


class PAClf(MetaClf):
    def __init__(self, **kwargs):
        super().__init__(classifier_instance=PassiveAggressiveClassifier(max_iter=1000, loss='squared_hinge'), **kwargs)

    def inference(self, input_text: str):
        vector = self.scaler.transform(self.emb.encode(input_text).reshape(1, -1))
        return self.clf.predict(vector)[0]

    def inference_proba(self, input_text: str):
        return self.inference(input_text)

    def predict_proba(self, array):
        return list(map(int, self.clf.predict(array)))