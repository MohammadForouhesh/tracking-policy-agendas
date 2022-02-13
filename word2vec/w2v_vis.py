from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np
import random


def reduce_dimensions(w2v_model):
    num_dimensions = 2
    vectors = np.asarray(w2v_model.wv.vectors)
    labels = np.asarray(w2v_model.wv.index_to_key)

    tsne = TSNE(n_components=num_dimensions, random_state=42)
    vectors = tsne.fit_transform(vectors)

    x_evals = [v[0] for v in vectors]
    y_evals = [v[1] for v in vectors]
    return x_evals, y_evals, labels


def plot_with_matplotlib(x_evals, y_evals, labels):
    random.seed(0)

    plt.figure(figsize=(12, 12))
    plt.scatter(x_evals, y_evals)
    indices = list(range(len(labels)))
    selected_indices = random.sample(indices, 25)
    for i in selected_indices:
        plt.annotate(labels[i], (x_evals[i], y_evals[i]))
    plt.savefig('w2v_plot.png')
    plt.show()


if __name__ == '__main__':
    from word2vec.w2v_corpus import W2VCorpus
    import pandas as pd
    import gensim.models
    corpus = pd.read_excel('test_corpus.xlsx')
    print(corpus.head())
    corpus = W2VCorpus(list(corpus[0]))
    model = gensim.models.Word2Vec(sentences=corpus)
    x_evals, y_evals, labels = reduce_dimensions(model)
    plot_with_matplotlib(x_evals, y_evals, labels)