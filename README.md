# Computational Political Science Papers Implementations
 This repository contains the implementation for the following papers:
 > [Tracking Legislators’ Expressed Policy Agendas in Real Time](https://osf.io/preprints/socarxiv/ync87/)

## TO-DO:

- [x] Summarizing the paper
- [x] Outlining the details of implementations
- [x] Implement Word2Vec
- [ ] Training Word2Vec
- [ ] Seed words
- [x] Classification heads
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

    1. Stump speeches: [Fenno 1978](https://profbrown.org/p/notes/fenno_homestyle)
    2. Campaign mail: [Golbeck, Grimes and Rogers 2010](https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.21344)
    3. Television advertising: [Lau, Sigelman and Rovner 2007](https://onlinelibrary.wiley.com/doi/10.1111/j.1468-2508.2007.00618.x)
    4. Floor speeches: [Martin and Vanberg 2008](https://www.jstor.org/stable/20299752); [Martin 2011](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1741-1130.2011.00316.x); [Quinn et al. 2010](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-5907.2009.00427.x)
    5. Press releases: [Grimmer 2010](https://econpapers.repec.org/article/cuppolals/v_3a18_3ay_3a2010_3ai_3a01_3ap_3a1-35_5f01.htm); [Grimmer, Westwood and Messing 2014](https://press.princeton.edu/books/hardcover/9780691162614/the-impression-of-influence); [Klüver and Sagarzazu 2016](https://www.researchgate.net/publication/258136850_Ideological_congruency_and_decision-making_speed_The_effect_of_partisanship_across_European_Union_institutions)
    6. Websites: [Adler, Gent and Overmeyer 1998](https://www.jstor.org/stable/440242); [Anstead and Chadwick 2008](http://www.handbook-of-internet-politics.com/pdfs/Nick_Anstead_Andrew_Chadwick_Parties_Election_Campaigning_and_Internet.pdf); [Druckman, Kifer and Parkin 2009](https://faculty.wcas.northwestern.edu/~jnd260/pub/Druckman%20Kifer%20Parkin%20APSR%202009.pdf)
    7. RSS feeds: [Cormack 2013](https://personal.stevens.edu/~lcormack/sins_of_omission_orig.pdf)
    8. Social media posts: [Gulati and Williams 2010](https://opensiuc.lib.siu.edu/pn_wp/43/); [Barbera et al. 2018](https://pubmed.ncbi.nlm.nih.gov/33303996/); [Radford and Sinclair 2016](https://www.semanticscholar.org/paper/Electronic-Homestyle-%3A-Tweeting-Ideology-∗-Radford-Sinclair/ac077dbf0040a13a4766f3f178c230fae4546b34); [Shapiro et al. 2014](https://m.japss.org/upload/1.%20Final%20Park.pdf); [Lilleker and Koc-Michalska 2013](https://journals.sagepub.com/doi/full/10.1177/1461444815616218)

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
  | | | <b> Elastic Net </b> | <b> 0.881 </b> | <b> 0.967 </b> | <b> 0.809 </b> | <b> 0.801 </b> | <b> 0.615 </b>
  | | | Lasso | 0.871 | 0.962 | 0.797 | 0.784 | 0.586
  | | Immigration (Inclusive or Not) | Naive Bayes | 0.892 | 0.865 | 0.920 | 0.830 | 0.781
  | | | XGBoost | 0.888 | 0.916 | 0.861 | 0.828 | 0.746
  | | | <b> Elastic Net </b> | <b> 0.890 </b> | <b> 0.978 </b> | <b> 0.817 </b> | <b> 0.821 </b> | <b> 0.674 </b>
  | | | Lasso | 0.894 | 0.974 | 0.826 | 0.828 | 0.691
  | | Climent Change (No Action or Not) | Naive Bayes | 0.889 | 0.874 | 0.904 | 0.827 | 0.742
  | | | XGBoost | 0.888 | 0.896 | 0.880 | 0.818 | 0.698
  | | | Elastic Net | 0.891 | 0.963 | 0.830 | 0.811 | 0.575
  | | | <b> Lasso </b> | <b> 0.892 </b> | <b> 0.965 </b> | <b> 0.830 </b> | <b> 0.813 </b> | <b> 0.576 </b>
  | | Climent Change (Take Action or Not) | Naive Bayes | 0.687 | 0.742 | 0.640 | 0.758 | 0.746
  | | | XGBoost | 0.678 | 0.694 | 0.662 | 0.736 | 0.729
  | | | <b> Elastic Net </b> | <b> 0.706 </b> | <b> 0.764 </b> | <b> 0.655 </b> | <b> 0.745 </b> | <b> 0.748 </b>
  | | | Lasso | 0.700 | 0.764 | 0.646 | 0.738 | 0.742

## Implementation details
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```




