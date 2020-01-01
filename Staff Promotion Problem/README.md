Project: Staff Promotion Prediction
The dataset can be gotten from https://www.kaggle.com/c/intercampusai2019.

You can test the fully functional web app on https://staff-promotion.herokuapp.com/


**Business Objectve**

This project aims to help employers/managers decide on what important feature are used to predict the eligibility of an employee promotion.

***The Project***

**EDA**

It is important to perform EDA on any data before going on to build a model.
- First, I created a new feature to represent the age and employee was employed into the company.
- Then filled all missing rows with correct details.
- I also made sure each feature had the correct data type.

Some Informaton I got during the EDA are:
1. Most employees are foreigned trained. 92% of employees schooled in a foreign school while 8% schooled in Ngeria (Unversity)
2. BUlk of the staff where Employed at 24. In range, the most employable age is between(23 - 27). Over 200 employees where employed within the age bracket.
3. No first degree holder is above 30 years of age.
4. The oldest employees usually have the highest qualification.
5. The oldest employees with the highest qualification are in the Regulatory and Legal Services Dvision.
6. Male Employees took part in more training than Female employees.

You can take a look at the EDA notebook for more analysis.

**Feature Selection**

So to get the most important features from the model, I first built a simple baseline random forest model after which I got the feature importance of each 
feature and selected features with values greater than 0.005. I did this so i could get the most important features useful in the 
decision making and make it easy for deployment.

After the feature selection the total number of features left where 7. I used 7 feature to build the model.

**Model**

The evaluation metric used was the F1 Score. Why? Because it has a better representation of our model, 
especally a classifier wth skewed dataset. It finds the balance between Precision and Recall.

I built a total of 5 models(Logistic Regression, KNearestNeighbor, SVM, RandomForest and XGboost Classifier.
- XGboost performed better than all the models when compared on our evaluation metric.
- It gave me a F! score of 92% and had the lowest number of misclassification.

XGboost was what was deployed. You can test the fully functional webapp on https://staff-promotion.herokuapp.com/
