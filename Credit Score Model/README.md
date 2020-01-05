# Credit Score Model.
- This repo contains all the files used to build a credit score model.
- Try out the model https://credit-score-model.herokuapp.com/
## Data Analysis
1. #### Loan Distribution.
- Firstly I analysed the distrbution for the loan amount, funded amount and funded amount investor.

![distribution](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/distribution.png)
There is a similar distribution between the 3 amount. Tells us that most of the requested loans where funded by the investors.

2. #### Loan Issued over the Years.
- What's the loan issue rate like since 2013?
![loans issued](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/loan%20issued.png)

There has been a general increase in loans issued from 2013.
- Notice that there's a steady increase in loans issued before mid 2015.
- From mid 2015 we can see a massive spike and a quick drop follows and this pattern is repeated till mid 2016.
- Post 2016 sees a more decent sideways movement in loans issued.

The general increase in loans can be as a result of good economic environments and as well as investors profitting from the interest on loans.

3. #### Let's look at the Interest Rate over the Years.
- Is there an Increase in interest rate?
![Interest Rate](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/interest%20rate.png)

- Pre 2013 sees a rise and drop in interest rate.
- On a more general note, we don't see a rise in interest. 
- Mid 2013 shows a steady drop in interest rate from  ~15.3% in mid 2013 to  ~12.3% in early 2016.
- There's a spke in interest rate in mid 2016 to  ~13.5%. This creates a sideways movement till a quick drop in 2018 to  ~15.3%.
- From 2018 we see a steady movement in the rates. The movement see interest rate staying between 13% and 12.5%.

I don't think the drop in interest rate can reduce the number on investors that are wlling and ready to fund more peer to peer loans.
But one thing is sure that it can result n more persons coming to get loans, this in turn will result in more profits for the investors funding the loans as long as people are able to fully pay back their loans.

4. #### Loan Status
- Are People Defaulting on their Loans?
![loan status](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/loan%20status.png)
- This looks good. We see that 48% have fully paid back the loans while 39% are current on their loans.
- Fully paid and Current are indicators of good loans, we can say that ~87% have paid back the loans. This is higher than I expected.
- Looking at the bad loans. We see that 13% of individuals either defaulted on the loans, are late toward payment or have loans charged off.
- This is high in some sense but the numbers can be brought down if the late payments come through.

Overall this shows a good indicator of loans having a high chance of being payed back but can also hurt some investors.

5. #### Loan Purpose
- Why Do People Take Loans?
![purpose](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/purpose.png)

- It's no surprise here that debt consolidaton and Credit Card refinancing are the major reasons why people take loans.
- These purpose account for over 70% of the loans collected.
- Home inprovements seems to be another major reason why people take loans.
- Small busnesses, purchases, car, moving, wedding education and others are also on the list.

6. #### Income Distribution
- Are High Income Earners Taking Loans?
![high earners](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/highearners.png)

High Income earners are chosen as individuals with annual income above $150k.
- We can see that the top 10 high income earners are Directors, VP's, CEO's, General Managers and Owners etc.
- Directors top the list followed by VP's and Presidents.
- Other high earners are Physician, Attorneys, Sales, Managers.

- What about Low Annual Income?
![low income](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/low%20earners.png)
- We can also find Onwers, Sales and Managers on this list.
- Others are Registered Nurse, Office Managers, Drivers, Teachers, Supervisors and Project Managers.

7. #### Income Distribution For Top-Top Earners.
- How's the annaul income distrbuted among Top Earners.
![top income](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/high%20income.png)
- For the top 4 earners, we can see that the annual income is skewed to the left, this shows that majority of the earners earn between
$150k to $500k annualy.
- The outliers shows the highest annual earners for the top earners and their annual income are as follows.
  - Director is $8 million.
  - President is $4 million.
  - VP is $2.5 million.
  - Owner is $2 million.
  
 8. #### Loan Amounts of Top Earners.
 - What's the distribution of loans collected by top earners?
 ![top loans](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/high%20loan.png)
 
 - We can see that the loan amount have similar distributon.
 - In all the distribution. Loan amount between $30k and $40k has been collected the most.
 
 
## Model Building

- Building a credit risk model.
- This model will assign a risk rating to a potential loan applicant.
- The model will assign ratings(Excellent, Good, Fair and Bad)
** Business prospect **
- This model will help investors in deciding on which loans to fund and loans to ignore.

### Setting Up the Project.
- Determine the problem.
- Choose Evalutaion Metric.
- Data Processing
- Feature Selection
- Model Building and Evaluation
- Predict Probability on Evaluaton Set.
- Create A New Columns For the Ratings on Evaluation Set.

### Determine the Problem

- Creating a  credit risk model is a binary classification model.

This means we are going to create a binary classification model. Where we use the model probabilty prediction to determine the ratng of each loan. 

- Ratings below < 0.25 are considered Bad.
- Ratings between 0.25 and 0.5 are consiidered fair.
- Ratings between 0.5 and 0.75 are consdered Good.
- Ratings above 0.75 are considered excellent.

### Choose Evaluation Metric

- The evaluation metric for this project will be the f1 Score because our data label is highly imbalanced/Skewed.

    1       1431855
    
    0       220597

### Data Processing and Feature Selection

- Firstly, Read the Data.
- The Data contains about 151 features and 2.2 million training set.
- Since we have over 2 million training set and 151 features, I won't be doing much feature engineering.
- Drop all missing columns and rows. This will help with making the training process faster and reduce computational power. Note I dropped columns with more than 30% missing values.
- After dropping mssing columns, I am left with 93 features and 1.6 millons training example. I still have a lot of data to play wth.
- Check the cardinality of features and drop the feature with only a single value and features with more unique values. For example Id columns, Url, Zip code, emp_title etc.
- Drop all the datetime columns becuase they require a lot of engineering and add litte improvement in terms of performance.

- Perform label encoding on all the categorical features.
- Check the corellation of all the numeric features in the data and drop one of the corresponding features with high correlation. This will help prevent overfitting.
- For the class label, Originally the loan status contains 7 categorical features. Combined them into two categorical features. Good loans and bad loans.
- Good loans is the combination of Fully Paid and Current loans
- Bad loans is the combination of Charged off, Late, In grace period and Default loans.
- Finally Split the data into Train, Test and Validation.
- The split ratio is 90%, 1%, 1%.

### Model Building and Evaluation

- Use the Xgboost algorithm to build the model. No hyperparameter tuning was carried.
- After training the model on the training set and test on the test set we checked 
- The model performance on our test set is 98% and checking the classification the model predict the both classes well.

Classification Matrix


![matrx](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/matrix.png)


Precision Recall Plot


![pr](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/auc.png)

The precision recall plot shows that our model performance is good. 98%


ROC-AUC Plot


![roc](https://github.com/geewynn/Machine-Learning-Project/blob/master/Credit%20Score%20Model/images/fpr.png)


For our Final task, We get the probablity of each prediction and assign the ratings to each prediction probability as described above.

After dong the above, There was a total of 142358 Excellent Rating, 17886 Bad loans, 3514 Good loans, 1488 Fair loans.
