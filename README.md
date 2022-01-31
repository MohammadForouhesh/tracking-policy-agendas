# Computational Political Science Papers Implementations
 This repository contains the implementation for the following papers:
 > [Tracking Legislators’ Expressed Policy Agendas in Real Time](https://osf.io/preprints/socarxiv/ync87/)

## TO-DO:

- [x] Summarizing the paper
- [x] Outlining the details of implementations
- [ ] Implement Word2Vec
- [ ] Training Word2Vec
- [ ] Seed words
- [ ] Classification heads
- [ ] Topic modeling
- [ ] Results & Analysis

## A Brief Summary of The Papers
### 1) Tracking Legislators’ Expressed Policy Agendas in Real Time
* #### Introduction:
  <div style="text-align: justify"> This work aims to analyse political orientation of legislators on salient policy issues through their temporally granular tweets, using a word embedding for feature extraction, and a classifier to label all legislators’ past and current relevant tweets according to whether they express a particular issue position over time. </div> 
* #### Main Problem:
    <div style="text-align: justify"> Is it possible to accurately analyse the temporal evolution of political orientation on salient issues by applying natural language processing techniques on users tweets? </div> 

    <div style="text-align: justify"> The issues of concern in this paper are <b> immigration</b>, and <b>climate change</b>.  </div>
* #### Illustrative Example:
    <div style="text-align: justify"> Given a tweet about immigration policy, they first encode it using word2vec enhanced dictionary, then its exclusiveness or inclusiveness can be detected using a classifier. Furthermore these results can be disaggregated to see whether it was posted from a Republican or a Democrat.  </div>
* #### I/O:
  * Input: Tweets (textual modality)
  * Output: Predicted stance on the salient political issue

* #### Motivation:
    1. <div style="text-align: justify"> Using tweets to track shifts in legislators’ rhetoric is highly scalable. It can be used on any topic of interest, by any political actor with a Twitter account, in any country around the world, from the past decade or into the future. </div> 
    2. <div style="text-align: justify"> Twitter data has high temporal granularity. </div>

* #### Related (Previous) Works:
    According to legislator’s different channels of communications, it is divided into 8 categories:

    1. Stump speeches: [Fenno 1978]()
    2. Campaign mail: [Golbeck, Grimes and Rogers 2010]()
    3. Television advertising: [Lau, Sigelman and Rovner 2007]()
    4. Floor speeches: [Martin and Vanberg 2008](); [Martin 2011](); [Quinn et al. 2010]()
    5. Press releases: [Grimmer 2010](), [2013b](); [Grimmer, Westwood and Messing 2014](); [Klüver and Sagarzazu 2016]()
    6. Websites: [Adler](), [Gent and Overmeyer 1998](); [Anstead and Chadwick 2008](); [Druckman, Kifer and Parkin 2009]()
    7. RSS feeds: [Cormack 2013]()
    8. Social media posts: [Gulati and Williams 2010](); [Barbera et al. 2018](); [Radford and Sinclair 2016](); [Shapiro et al. 2014](); [Lilleker and Koc-Michalska 2013]()

* #### Contributions of this paper:
    1. <div style="text-align: justify"> Simple, transparent, and interpretable approach to tweet classification can achieve satisfactory levels of accuracy across diverse issues. </div>
    2. <div style="text-align: justify"> Automate the process of updating and maintaining the model. </div>
    3. <div style="text-align: justify"> Develop a dynamical, real-time scalable method for tracking elected officials’ expressed policy positions through their tweets. </div> 

* #### Proposed Method:
    * ##### Stage I: (Feature Extraction)
        <div style="text-align: justify"> They used Word2Vec enhanced dictionary to encode the texts. In particular, a set of stemmed seed words is identified as being relevant to the concept of interest. Then use word embeddings to identify other words that are semantically related to these seed words in the data. </div>

    * ##### Stage II: Classification of political stance on salient issues.
        <div style="text-align: justify"> Choice of classifier: using five-fold cross validation and comparing precision, recall, accuracy, balanced accuracy, and F1 scores to choose the best performing classifier among XGBoost, Naive Bayes, Elastic Net, Lasso. </div>

* #### Experiments:
    * ##### Datasets:
      Their own making. Crawled all senators and the vast majority of members of the House tweets using twitter API from any period of interest up to 2020, excluding those who left office or were elected for the first time.

    * ##### Results:
      Trained word embeddings on the entire corpus of legislators’ tweets. The word2vec dictionaries are limited to the 100 most similar words to the seed words and overly general or irrelevant terms are omitted. 
      The detailed results provided in the appendix is summarised in the below table:
  
| Dataset | Issue | Classification Method | F1-score | Recall | Precision | Accuracy | Balanced Accuracy|
|---------|-------|-----------------------|----------|--------|-----------|----------|------------------|
| Crawled Legislators' Tweets | Immigration (Exclusive or Not) | Naive Bayes | 0.885 | 0.853 | 0.921 | 0.813 | 0.738
| | | XGBoost | 0.871 | 0.909 | 0.836 | 0.795 | 0.668
| | | Elastic Net | 0.881 | 0.967 | 0.809 | 0.801 | 0.615
| | | Lasso | 0.871 | 0.962 | 0.797 | 0.784 | 0.586
| | Immigration (Inclusive or Not) | Naive Bayes | 0.892 | 0.865 | 0.920 | 0.830 | 0.781
| | | XGBoost | 0.888 | 0.916 | 0.861 | 0.828 | 0.746
| | | Elastic Net | 0.890 | 0.978 | 0.817 | 0.821 | 0.674
| | | Lasso | 0.894 | 0.974 | 0.826 | 0.828 | 0.691
| | Climent Change (No Action or Not) | Naive Bayes | 0.889 | 0.874 | 0.904 | 0.827 | 0.742
| | | XGBoost | 0.888 | 0.896 | 0.880 | 0.818 | 0.698
| | | Elastic Net | 0.891 | 0.963 | 0.830 | 0.811 | 0.575
| | | Lasso | 0.892 | 0.965 | 0.830 | 0.813 | 0.576
| | Climent Change (Take Action or Not) | Naive Bayes | 0.687 | 0.742 | 0.640 | 0.758 | 0.746
| | | XGBoost | 0.678 | 0.694 | 0.662 | 0.736 | 0.729
| | | Elastic Net | 0.706 | 0.764 | 0.655 | 0.745 | 0.748
| | | Lasso | 0.700 | 0.764 | 0.646 | 0.738 | 0.742









