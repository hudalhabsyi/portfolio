# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2: Singapore Housing Modelling


## 1. Introduction
The Housing Development Board (HDB) was setup to tackle the housing crisis in 1960s and now serves as the sole agency for public housing. HDB homes more than 80% of Singapore residents, across 24 towns and 3 estates. Key features of HDB’s public housing policy includes the sale of public houses to residents, but with a limited 99 year lease and it can be bought back by the government.

The Singapore Housing Dataset contains historical data related to resale transactions for Housing Development Board (HDB) flats that took place between the period of March 2012 to April 2021. 

Besides information on resale prices and transaction details, the dataset contains over 70 variables related to location and age of the units, their physical specifications, corresponding storey levels and dwelling mix within the flats, as well as the availability of various amenities (e.g. malls, hawkers, transport, schools).

## 2. Problem Statement of Project
As property buyers in Singapore, the affordability of a HDB unit and potential factors that can influence the price are of interest because this can guide them in their planning process before making a purchase.

We make use of a regression model to give insights to prospective buyers on factors relating to the HDB unit that affect resale prices.

## 3. Datasets
The following data sets will be used for the project obtained from [Kaggle](https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/data).
1. train.csv
    - contains variables ranging from housing specifications to amenities for 150,634 HDB flats from 2012 to 2021
2. test.csv
    - similar to train.csv, excluding the resale prices of the HDB 
    - contain details for 16,737 HDB  flats from 2012 to 2021


 ### Data dictionary:

 This data dictionary contains features that were engineered from the original dataset. Features not found here can be found in the original dataset using the link [here](https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/data).

|Feature|Type|Description|
|---|---|---|
|town_region|object|feature engineered by recategorizing "town" column - HDB township where the flat is located| 
|hdb_age_when_sold|int64|feature engineered by subtracting lease_commence_date from tranc_year|
|units_per_floor|float64|feature engineered by dividing total_dwelling_units by max_floor_lvl|
|has_rental|int32|feature engineered for boolean value if there is rental units in the same block
|standard_models|object|combination of flat models: standard, new generation, simplified, model A, model A2, improved, apartment, premium apartment|
|maisonette_models|object|combination of flat models: maisonette, improved-maisonette, model A maisonette, premium maisonette, premium apartment loft|
|private_design_models|object|combination of flat models: DBSS, type s1, type s2|

## 4. Summary of Analysis
### (a) Model Selection
**Ridge regularization** is chosen to be the model of choice.

Using Linear Regression as the baseline, even though it seems that Lasso regularization will be the optimal choice as it has produced better R2 scores on both the training and test sets as well as K-fold cross validation scores, it has the highest RMSE value out of the 3 models.

On the other hand, even though Ridge regularization has slightly higher R2 scores, it still performed better than linear regression. The train and test score difference is considered minimal - it means that the model still trained sufficiently well and there is only a very slight overfit on the test data. Most importantly, out of the 3 models, Ridge regularization has the lowest RMSE score - this is important as we would want a lower score so that the predicted resale prices would have a lower margin of error compared to the actual resale prices.

### (b) Results from model
The top 3 features that influence resale prices are:
- town region North
- town region West
- town region North-east


## 5. Recommendations
Based on our problem statement, we came up with recommendations for 3 potential groups of buyers: 
1. Budget-conscious
- To consider purchasing units in the North region of Singapore as it generally has the lowest prices compared to the other regions, if location is not a concern
- Likely due to towns in the North are non mature

2. Family-oriented
- To consider 4-room, 5-room and executive flat types 
- Can still cost-save by considering units the North, West and North-east regions

3. Design-conscious
- To consider looking at flat models instead of flat types and locations
- Maisonette and private built flat models have bigger floor area, "luxurious feel"
- However the trade-off is that prices might be higher than the standard HDB units

However there are also other potential factors that buyers can consider which are not
- Noise i.e. surrounding ambient noise of the unit
- HDB measures i.e. cooling measures, eligibility controls, ethnic quotas
- Other preferential & community features i.e. corner units, orientation of unit, proximity to community amenities

## 6. Conclusion of recommendations
1. Top considerations are regions and maturity of the estate that the HDB unit is located in
2. Followed by the unit specifications of flat type, flat model, floor area
3. Personal preferences
However, since HDB units are still under purview of public housing policy and the resale market is subject to policy changes and circumstances, buyers will have to keep these in mind.


## 7. Sources of information for further research
1. [Mature vs Non mature towns in Singapore](https://www.hdb.gov.sg/-/media/doc/CCG/20082023-Annexes/Annex-A1.ashx)
2. [Town areas segregated by HDB](https://www.hdb.gov.sg/about-us/history/hdb-towns-your-home)
3. [Summary of cooling measures on HDB prices](https://www.businesstimes.com.sg/property/mobile-spotlight/summary-singapores-property-cooling-measures-1996-present-day)
4. [Effect of cooling measures on HDB prices in 2013 and 2018](https://www.channelnewsasia.com/singapore/property-cooling-measures-hdb-resale-prices-2013-2018-each-singapore-town-2385831)
5. [Ethnic Quota effect on selling and buying HDB](https://www.propertyguru.com.sg/property-guides/how-the-ethnic-quota-can-affect-your-sellingbuying-ability-6747)
6. [Living with noise pollution: Serangoon, Bukit Timah and Clementi among the noisiest neighbourhoods in Singapore](https://www.straitstimes.com/singapore/housing/sounds-awful-cant-sleep-cant-talk-because-of-noise)
7. [Outside noise could affect home prices](https://cos.sg/blog-post/outside-noise-could-affect-home-prices/)
