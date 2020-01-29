# NewYork Yellow Taxi Ride Tip Prediction Machine Learning Project

## Project Overview
- The Dataset is the NewYork Yellow Ride Dataset gotten from
- It contains over 7 million rows and 17 columns
- This is a pure machine learning project to predict the tip price given to taxi drivers after each ride.
- This project was built with 5 solid Machine Learning Project on which some regularization and feature selection was carried out.

## Project Structure
- 1. Business Usecase.
- 2. Choose Evaluation Metric.
- 3. Data Analysis(EDA).
- 4. Data Preprocessing.
- 4. Model Building.
- 6. Feature Selection

### Business Approach.
- The business approach here is to help solve the problem of tip amount given to drivers after a ride. This will guide both riders and drivers to get the exact amount or close to exact amount rather than trying to use emotions to determine the tip amount.

### Evaluation Metric
- This is Purely a Supervision Problem and a Regression Problem.
- The major evaluation metric used in this project is the Root Mean Square Error. Although other metric such as R_square and Mean Square Error are shown in the notebook.

### Data Anlytics
- Check the [EDA](https://github.com/geewynn/Machine-Learning-Project/blob/master/New%20York%20Trip/trip_analysis.ipynb) for more data anlytics.

### Data Preprocessing

#### Missing Values
  - A columns had over 60% missing values. The best decision was to drop them off since the dataset was large.

#### Outliers

- There where situations in the data set with unfair outliers. This outliers skewed our datset and had to be dropped.
  - Dropped fare amount greater than 5000.
  - Dropped trip distance greater than 200 miles.
  - Dropped instances that had trip amount greater than 0 and distance was 0 miles.
  
#### Datetime Columns
- Converted the datetime columns to datetime.
- Created fetaures such as dropoff/pickup(time, date and hour).
- Created a new feature from the created feature called dropoff/pickup time period bin the hour columns into time of the day.(Morning, afternoon and Night).
- Drop instances where pickupdate was greater than dropoff date.
- Drop datetime columns used to create new features.

#### Categorical Data
- For the categorical columns, they where label encoded to and represented by numerical figures.

#### Data Split
- The data was split into train, test split.
- The split was done in the ratio of 80, 10, 10
- 80 for training, 10 for test and 10 for validation.

### Model Building
- 5 Models where used and a comparison of those models will be done.
- The models are as follows
  - Linear Regression
  - Elastic Net
  - LassoCV
  - Decision Tree Regressor
  - Gradient Boosting Regressor

#### Linear Regression
- After the model was instatiated and fit on the training set and after the prediction on the test set. It produced,
  - The model explained 99.8% of the variance in the train set and 99.8% of the variance in the test set.
  - A RMSE score of 9.81 which is a bit decent on the first try.
  - Lasso regularization with an alpha = 0.4 compressed all the features to zero.
  
  ##### Residual Plot for Linear Regression Model.
    ![residual](https://github.com/geewynn/Machine-Learning-Project/blob/master/New%20York%20Trip/images/residual.png)
    - The plot shows a clear pattern with the line being stationary at zero. This can mean that our data is not a random data set and also not linear and might need a non-linear model.
  
  ##### Fetaure Selection for Modellling with LassoCV
  - The LassoCv model selection package was used to carry out feature selection for modelling.
  - The model selected 10 features out of the original 16. 
  - It compressed the non-selected feature coeficient to 0.
  
    | Columns  | LassoCV coeficient |
    | ------------- | ------------- |
    | VendorID  | -0.0013343364494424247  |
    | payment_type   | -0.177  |
    | fare_amount   | -10.079  |
    | extras   |  -0.4534  |
    | mta_tax  |  -0.0469  |
    | tolls_amount  | -1.971  |
    | improvement_surchage   |  -0.0216  |
    | total_amount  | 13.387  |
    | dropoff_time_period  |  5.910   |
    | pickup_time_period  |  0.0  |
    | passenger_count  |-0.0  |
    | trip_distance | 0.0   |
    | RatecodeId  | -0.0  |
    | store_and_fwd_flag  | 0.0   |
    | PULocation   |  0.0   |
    | DOLocation   | 0.0   |
    
 - The top 10 are the selected features for modelling in our linear Regression model, while the bottom six are the compressed features that where rejected.
    
 - From the LassoCV table:
      - total_amount had the highest coefficient which also means it plays a big role in predicting the tip amount.
      - Drop_off time follows with the second largest coefficient.
 - Linear regression model has an intercept of 1.81.
 
 
 
#### ElasticNet Model
- Baseline elastic net model produced:
  
  | Metric  | Score |
  | -------- | ------- |
  | r_squared score | 0.88 |
  |MSE | 0.69 |
  | RMSE | 0.83   |

- The elasticnet model produced the following residual plot
    ![elastic](https://github.com/geewynn/Machine-Learning-Project/blob/master/New%20York%20Trip/images/elastic.png)

##### Tuned ElasticNet Model
- Tuned the elasticNet model with a GridSearchCV
- Specifically, only the l1_ratio was tuned with a l1_ratio of 1.0 as the best parameter.
- The tuned model produced:

    | Metric  | Score |
    | -------- | ------- |
    | r_squared score | 0.99 |
    |MSE | 0.03 |
    | RMSE | 0.199   |
      
 - The tuned model produced better scores compared to the baseline elasticnet model.
 
 - Seeing the results from the linear models can tree based models perform any better?
 
#### Decision Tree Regressor
##### Baseline Model

- The baseline model produced the following scores

    | Metric  | Score |
    | -------- | ------- |
    | r_squared score | 0.97 |
    |MSE | 0.16 |
    | RMSE | 0.41   |
    
 - The baseline decision tree model performance was impressive, better than both linear models. Although, the RMSE score can be improved on.
 
 
 #### Gradient Boosting Regressor
 - Scores produced by the model 
 
     | Metric  | Score |
    | -------- | ------- |
    | r_squared score | 0.99 |
    |MSE | 0.03 |
    | RMSE | 0.574   |
- This performed poorly compared to the Decision Tree model. What Kind of features will it select.

#### Gradient Boosting Regressor With RFE
- Trained a RFE to select 10 features and drop 2 features after each step.
- The RFE produced the following mask after over 30 minutes of training.

     | Columns  | LassoCV coeficient |
     | ------------- | ------------- | 
     | payment_type   | True  |
     | fare_amount   | True |
     | extras   |  True  |  
     | tolls_amount  | True  |
     | improvement_surchage   | True  |
     | total_amount  | True  |   
     | trip_distance | True   |
     | RatecodeId  | True  |
     | store_and_fwd_flag  | False   |
     | PULocation   |  True   |
     | DOLocation   | True   |
     | VendorID  | False  |
     | mta_tax  |  False  |
     | dropoff_time_period  |  False   |
     | pickup_time_period  |  False  |
     | passenger_count  | False  |
    
 - From the abpve table the columns with True are the selected columns while the rest where dropped.
 
 - For detailed information. Chacke out the complete notebook (https://github.com/geewynn/Machine-Learning-Project/blob/master/New%20York%20Trip/Yellow_Ride_Model.ipynb)
