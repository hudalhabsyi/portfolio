# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs & NLP

# Executive Summary
> SG-DSI-41 Group 01: Daryl Chia, Germaine Choo, Sharifah Nurulhuda, Tan Wei Chiong

---
**Problem Statement**
---

Our project aims to distinguish between Millennials (1981-1996) and those from Generation Z (Gen Zs) (1997-2010) by their language use: what they say and how they say it. Specifically, we are targeting companies who advertise on Instagram so as to empower them with the option to see the proportion of Gen Zs and Millennials that are actually engaging with their posts through comments. This will allow such companies evaluate their advertising strategies accordingly.

Gen Zs and Millennials spend the most time on social media, comprising 75% of those who spend 5 hours or more a day on it. They are also more than twice as likely to purchase products after seeing advertisements on such platforms. As such, it will be assumed that the bulk and majority of users commenting on instagram advertisement posts are Gen Zs and Millennials accordingly.

To distinguish between them, we will be building and evaluating classifier prediction models to make the binary prediction on who a given instagram comment is written by: Gen Z (1) or Millennial (0). Specifically, we will be looking at:

1. Bernoulli Naive Bayes (TF-IDF Vectorizer with 50k max features)
2. Bernoulli Naive Bayes (TF-IDF Vectorizer with 50k max features)
3. Multinomial Naive Bayes (TF-IDF Vectorizer with 50k max features)
4. Multinomial Naive Bayes (TF-IDF Vectorizer with 50k max features)
5. Logistic Regression (TF-IDF Vectorizer with 50k max features/ LASSO Regularization/ α=1)
6. Logistic Regression (TF-IDF Vectorizer with 50k max features/ LASSO Regularization/ α=10)
7. Logistic Regression (TF-IDF Vectorizer with 50k max features/ Ridge Regularization/ α=1)
8. Logistic Regression (TF-IDF Vectorizer with 50k max features/ Ridge Regularization/ α=10)

These models will be evaluated according to Accuracy since both target classes of Millennial or Gen Z are equally important for targeted advertisement strategy.

**Data Collection**
---

As a proxy for Millennial and Gen Z Instagram comments, we have performed web scraping on top post comments for the most popular Gen Z (r/GenZ) and Millennial (r/Millennials) Reddit subredits, under the premise that those who enanged with these subreddits through comments are primarily of that group.

Total comments scraped from 100 posts each:
- Gen Z: 38065
- Millennial: 48145

The amount of comments scraped provided a large enough dataset for our models to train and test on. Furthermore, these comments came from 100 posts each, which was well within what was permitted for scraping. The amount of posts scrapped for comments was sufficiently small to avoid being throttled or blocked by the Reddit server.

Work Flow (Web Scraping):
1. **Notebook 01_Web_Scraping**:
    - Scrape comments and threads from r/GenZ and r/Millennials into their respective data frames
    - Export data frames into .csv files.
2. **Notebook 01a_Combining_Comments**:
    - Load Gen Z and Millennial comment .csv files as data frames
    - Combine data frames into a single one
    - Export comments .csv file

## Data Cleaning and EDA
---

Total observations: 86210

Millennials (`generation_z` = 0): 48145

Generation Z (`generation_z` = 1): 38065


The data cleaning mainly involved removing comments that have no interpretive value and for those that do, replacing substrings wiwthin them that have no interpretive value. In other words, our analysis and prediction models would focus on n-gram words.

**Issues Checked For**
1. Null comments
2. Deleted comments
3. Removed comments
4. Bot comments
5. Comments with line or tab characters
6. Comments with redaction substrings
7. Comments with urls
8. Comments with html hexadecimal codes
9. Comments with Emoji hexadecimal codes
10. Comments with gif image codes
11. Comments with Reddit subredit references
12. Comments with Reddit username references
13. Comments with hashtags
14. Comments with numbers
15. Comments with bracket characters
16. Comments with punctuations, excluding apostrophes
17. Comments with extra whitespaces

**Follow-Up Actions**

Drop rows with:
 - Null comments
 - Deleted comments
 - Removed comments
 - Bot comments

Replace these substrings with a single whitespace:
 - Line or tab characters
 - Redaction substrings
 - urls
 - html hexadecimal codes
 - Emoji hexadecimal codes
 - gif image codes
 - Reddit subreddit references
 - Reddit username references
 - Numbers, including decade references.
 - Bracket characters
 - Punctuation

Others:
 - Standardize apostrophes
 - Remove trailing whitespaces
 - Drop empty string comments

The Exploratory Data Analysis (EDA) focused on analysing:
1. Comment Length & Word Count
    - Summary Statistic
    - Preview of shortest and longest strings by length and word count
    - Distribution of shortest and longest strings by length and word count
    - Findings: Millennials comments have a higher mean and wider spread for both measures
2. Percentage of Correctly Spelled Words in Comments
    - Generate distribution of percentage of correctly spelled words in a string
    - Finding: Millennials have a higher mean of percentage of correctly spelled words a string
3. Top Key Words for 1-gram, 2-gram, and 3-gram Words
    - In addition to the standard english stop words, additional common words were added in to tease out the key words that have interpretive value.
    - Seperate TF-IDF vectorizations were done for analysing 1-gram, 2-gram, and 3-gram words respectively. This was done to constrain the results in the case of 2-gram and 3-gram words.
    - Beyond that, the TF-IDF vectorizers had their maximum document frequency set at 3% to tease out other common words apart from stop words.
    - Finding: 1-gram words tend to be very simmilar, with similar top key words such as 'boomer', a generation term.
    - Finding: 2-gram words are relatively less similar than 1-gram words, with similar top key words such as 'social media', and different top key words such as 'net neutrality' for Generation Z, a term about internet freedom, and 'mental health' for Millennials.
    - Finding: 3-gram words are even less similar and most telling of lifestyle, with different top key words such as 'playing video games' for Generation Z, and 'living paycheck paycheck' for Millennials, a phrase that was likely 'living paycheck to paycheck'** before removing stop words.

Outliers were not removed since the dataset was significantly large, minimizing the bias of large comments driven by specific users.

## Preprocessing and Modelling
---

**Preprocessing**
1. Undersample Majority Class Data
    - Undersample majority class (`generation_z` = 0) to balance classes in the data
2. Stem Comment Words
3. Perform Train Test Split
4. Word Vectorize Comments
    - stop words removed
    - n-gram range: n=1-3
    - Keep apostrophes in word vectorization to include contraction words (e.g. "don't")
    - Tune Word vectorizors by varying `max_features` by 25000 and 50000.

**Modelling**

Fit models:

1. Bernoulli Naive Bayes (TF-IDF Vectorizer with 50k max features)
2. Bernoulli Naive Bayes (TF-IDF Vectorizer with 50k max features)
3. Multinomial Naive Bayes (TF-IDF Vectorizer with 50k max features)
4. Multinomial Naive Bayes (TF-IDF Vectorizer with 50k max features)
5. Logistic Regression (TF-IDF Vectorizer with 50k max features/ LASSO Regularization/ α=1)
6. Logistic Regression (TF-IDF Vectorizer with 50k max features/ LASSO Regularization/ α=10)
7. Logistic Regression (TF-IDF Vectorizer with 50k max features/ Ridge Regularization/ α=1)
8. Logistic Regression (TF-IDF Vectorizer with 50k max features/ Ridge Regularization/ α=10)

Results:

|   |**Classifier**|**TF-IDF Vectorizer**|**Regularization**|**Penalty Term ($α$)**|**Accuracy (Training Set)**|**Accuracy (Testing Set)**|
|---|---|---|---|---|---|---|
|1|Bernoulli Naive Bayes |Vectorizer 1 (50k max_features)|-|-|0.73|0.69|
|2|Bernoulli Naive Bayes |Vectorizer 2 (25k max_features)|-|-|0.71|0.70|
|3|Multinomial Naive Bayes |Vectorizer 1 (50k max_features)|-|-|0.84|0.76|
|4|Multinomial Naive Bayes |Vectorizer 2 (25k max_features)|-|-|0.81|0.76|
|5|Logistic Regression|Vectorizer 1 (50k max_features)|LASSO (l1)|1|0.79|0.75|
|6|Logistic Regression|Vectorizer 1 (50k max_features)|LASSO (l1)|10|0.69|0.68|
|7|Logistic Regression|Vectorizer 1 (50k max_features)|Ridge (l2)|1|0.85|0.76|
|8|Logistic Regression|Vectorizer 1 (50k max_features)|Ridge (l2)|10|0.77|0.74|

## Evaluation and Conceptual Understanding
---
- Different models were evaluated using accuracy, since there was no target class of interest, strictly speaking.
- The baseline score was the training set accuracy scores and all models show a degree of overfitting, but the deviation was not too far off with the testing scores.
- Colloquial cultural domain knowledge allowed us to interpret the key words based on both common themes and themes unique to each group.
- The Logistic Regression model with Ridge regularization and α = 1 was used as the best model since it had the highest accuracy score (76%).

## Conclusion and Recommendations
---
- Best Model: Logistic Regression model with Ridge regularization and α = 1 (76% accuracy)
- The best model was further evaluated in a demonstration of 10 selected other comments from the similar subreddits and demonstrated an 80% accuracy score. This demonstrated the usefulness of our model especially since "unintuitive" comments were chosen to test the robustness and generalizability of our chosen model.