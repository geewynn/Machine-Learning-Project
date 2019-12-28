import pickle

from xgboost import XGBClassifier
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

model = pickle.load(open('xgb_model.sav', 'rb'))


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 7)
    loaded_model = pickle.load(open("model.sav", "rb"))
    result = loaded_model.predict(to_predict)
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
        if int(results) == 1:
            #prediction = 'Congratulation, You have been promoted'
            return render_template("congrats.html")#, prediction=prediction)
        else:
            #prediction = 'Sorry. Improve on your current task'
            return render_template("sorry.html")#, prediction=prediction)


if __name__ == '__main__':
    app.run()
