import pickle

from xgboost import XGBClassifier
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)


# model = pickle.load(open('credit_model.sav', 'rb'))


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 8)
    loaded_model = pickle.load(open("credit_model1.sav", "rb"))
    result = loaded_model.predict_proba(to_predict)[:, 1]
    return result[0]


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        results = ValuePredictor(to_predict_list)

        if results <= 0.25:
         #   prediction = 'Bad Loan'  + ' ' + str(results)
           return render_template("sorry.html")
        elif 0.25 < results <= 0.5:
            return render_template("result.html")
            #prediction = 'Fair Loan' + ' ' + str(results)
        elif 0.5 < results <= 0.75:
            return render_template("congrats.html")
            #prediction = 'Good Loan' + ' ' + str(results)
        else:
            return render_template("excelent.html")
            #prediction = 'Excellent' + ' ' + str(results)

        #return prediction


if __name__ == '__main__':
    app.run()