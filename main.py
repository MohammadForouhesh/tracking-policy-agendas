import numpy as np
import pandas as pd
from tqdm import tqdm
from classifiers.pa_clf import PAClf
from classifiers.xgb_clf import XgbClf
from classifiers.lasso_clf import LassoClf
from classifiers.naive_bayes_clf import GNBClf
from preprocess.preprocessing import remove_emoji, remove_redundant_characters
from word2vec.w2v_vis import reduce_dimensions, plot_with_matplotlib

tqdm.pandas()


def inference_pipeline(model_path: str, input_text: str):
    xgb = XgbClf(text_array=None, labels=None, load_path=model_path)
    # return xgb.inference(input_text)
    return xgb.inference_proba(input_text)


def main(embedding_frame:pd.DataFrame, dataframe: pd.DataFrame, save_path: str):
    xgb = XgbClf(text_array=dataframe.prep_text, labels=dataframe.label, embedding_doc=embedding_frame.prep_text)
    xgb.build()
    # x_evals, y_evals, labels = reduce_dimensions(xgb.emb.w2v_model)
    # plot_with_matplotlib(x_evals, y_evals, labels)
    xgb.save_model(save_path)
    xgb = GNBClf(text_array=dataframe.prep_text, labels=dataframe.label, embedding_doc=embedding_frame.prep_text)
    xgb.build()
    # x_evals, y_evals, labels = reduce_dimensions(xgb.emb.w2v_model)
    # plot_with_matplotlib(x_evals, y_evals, labels)
    #xgb.save_model(save_path)
    xgb = PAClf(text_array=dataframe.prep_text, labels=dataframe.label, embedding_doc=embedding_frame.prep_text)
    xgb.build()
    x_evals, y_evals, labels = reduce_dimensions(xgb.emb.w2v_model)
    plot_with_matplotlib(x_evals, y_evals, labels)
    #xgb.save_model(save_path)


if __name__ == '__main__':
    df = pd.read_excel('vacine_sampling.xlsx')[['text', 'prep_text', 'label']]
    emb_df = pd.read_excel('clf_status_id_dummy.xlsx')
    print(emb_df.columns)
    emb_df = emb_df[emb_df.is__welfare == 1][['text', 'prep_text']]
    df['prep_text'] = df.prep_text.apply(lambda item: remove_redundant_characters(remove_emoji(item)))
    df = df.replace('', float('NaN')).dropna()
    emb_df['prep_text'] = emb_df.prep_text.apply(lambda item: remove_redundant_characters(remove_emoji(item)))
    emb_df = emb_df.replace('', float('NaN')).dropna()
    main(emb_df, df, 'vaccine')