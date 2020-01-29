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
- 4. Model Building.
- 5. Model Evaluation.
- 6. Feature Selection
- 7. Model Comparison.

### Business Approach.
- The business approach here is to help solve the problem of tip amount given to drivers after a ride. This will guide both riders and drivers to get the exact amount or close to exact amount rather than trying to use emotions to determine the tip amount.

### Evaluation Metric
- This is Purely a Supervision Problem and a Regression Problem.
- The major evaluation metric used in this project is the Root Mean Square Error. Although other metric such as R_square and Mean Square Error are shown in the notebook.

### Data Anlytics
- Check the [EDA](https://github.com/geewynn/Machine-Learning-Project/blob/master/New%20York%20Trip/trip_analysis.ipynb) for more data anlytics.

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
  - A RMSE score of 9.81 which is a bit decent on the first try
  - Lasso regularization with an alpha = 0.4 compressed all the features to zero.
  
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
      - total_amount had the highest coeficient which also means it plays a big role in predicting the tip amount.
      - Drop_off time follows with the second largest coeficient.
