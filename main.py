import pandas as pd
from tqdm import tqdm
from tracking_policy_agendas.classifiers.pa_clf import PAClf
from tracking_policy_agendas.classifiers.xgb_clf import XgbClf
from tracking_policy_agendas.classifiers.naive_bayes_clf import GNBClf
from tracking_policy_agendas.classifiers.lasso_clf import LassoClf
from tracking_policy_agendas.preprocess.preprocessing import remove_emoji, remove_redundant_characters

tqdm.pandas()


def inference_pipeline(model_path: str, input_text: str):
    xgb = XgbClf(text_array=None, labels=None, load_path=model_path)
    return xgb.predict(input_text)


def main(embedding_frame:pd.DataFrame, dataframe: pd.DataFrame, save_path: str):
    xgb = XgbClf(text_array=dataframe.prep_text, labels=dataframe.label, embedding_doc=embedding_frame.prep_text)
    xgb.fit()
    xgb.save_model('xgb_' + save_path)
    pa = PAClf(text_array=dataframe.prep_text, labels=dataframe.label, embedding_doc=embedding_frame.prep_text)
    pa.fit()
    pa.save_model('pa_' + save_path)
    lasso = LassoClf(text_array=dataframe.prep_text, labels=dataframe.label, embedding_doc=embedding_frame.prep_text)
    lasso.fit()
    lasso.save_model('lasso_' + save_path)
    gnb = GNBClf(text_array=dataframe.prep_text, labels=dataframe.label, embedding_doc=embedding_frame.prep_text)
    gnb.fit()
    gnb.save_model('gnb_' + save_path)


if __name__ == '__main__':
    df = pd.read_excel('vacine_sampling.xlsx')[['text', 'prep_text', 'label']]
    emb_df = pd.read_excel('clf_status_id_dummy.xlsx').sample(100000)
    emb_df = emb_df[emb_df.is__welfare == 1][['text', 'prep_text']]
    df['prep_text'] = df.prep_text.apply(lambda item: remove_redundant_characters(remove_emoji(item)))
    df = df.replace('', float('NaN')).dropna()
    emb_df['prep_text'] = emb_df.prep_text.apply(lambda item: remove_redundant_characters(remove_emoji(item)))
    emb_df = emb_df.replace('', float('NaN')).dropna()
    main(emb_df, df, 'vaccine')