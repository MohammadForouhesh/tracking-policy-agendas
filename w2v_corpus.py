from gensim import utils


class W2VCorpus:
    def __init__(self, corpus):
        self.corpus = corpus

    def __iter__(self):
        for line in self.corpus:
            yield utils.simple_preprocess(line)

