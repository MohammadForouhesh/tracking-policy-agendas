import pandas as pd
from sklearn.metrics import classification_report
from tqdm import tqdm

from classifiers.lasso_clf import LassoClf
from classifiers.naive_bayes_clf import GNBClf
from classifiers.pa_clf import PAClf
from classifiers.xgb_clf import XgbClf
from word2vec.w2v_vis import reduce_dimensions, plot_with_matplotlib

tqdm.pandas()


def inference_pipeline(model_path: str, input_text: str):
    xgb = XgbClf(text_array=None, labels=None, load_path=model_path)
    # return xgb.inference(input_text)
    return xgb.inference_proba(input_text)


def main(dataframe: pd.DataFrame, save_path: str):
    xgb = XgbClf(text_array=dataframe.text, labels=dataframe.label)
    xgb.build()
    x_evals, y_evals, labels = reduce_dimensions(xgb.emb.w2v_model)
    plot_with_matplotlib(x_evals, y_evals, labels)
    xgb.save_model(save_path)


if __name__ == '__main__':
    df = pd.read_excel('politics.xlsx')
    main(df, 'politics')