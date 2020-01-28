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
-
