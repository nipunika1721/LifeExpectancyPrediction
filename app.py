from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__, template_folder='Template')

# Load the trained model
#model = joblib.load("random_forest_model.pkl")
model = joblib.load("best_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        country = request.form['country']
        year = int(request.form['year'])
        status = request.form['status']
        adultmortality = float(request.form['adultmortality'])
        # infantdeaths = float(request.form['infantdeaths'])
        alcohol = float(request.form['alcohol'])
        # percentageexpenditure = float(request.form['percentageexpenditure'])
        # hepatitisB = float(request.form['hepatitisB'])
        # measles = float(request.form['measles'])
        bmi = float(request.form['bmi'])
        # underfivedeaths = float(request.form['underfivedeaths'])
        polio = float(request.form['polio'])
        # totalexpenditure = float(request.form['totalexpenditure'])
        diphtheria = float(request.form['diphtheria'])
        hivaids = float(request.form['hivaids'])
        gdp = float(request.form['gdp'])
        # population = float(request.form['population'])
        # thinness1to19years = float(request.form['thinness1to19years'])
        # thinness5to9years = float(request.form['thinness5to9years'])
        # incomecompositionofresources = float(request.form['incomecompositionofresources'])
        # schooling = float(request.form['schooling'])

        # Transform input features
        # features = np.array([year, adultmortality, infantdeaths, alcohol,percentageexpenditure,hepatitisB,measles, bmi, underfivedeaths, polio,totalexpenditure, diphtheria, hivaids, gdp, population,thinness5to9years,thinness1to19years, incomecompositionofresources, schooling]).reshape(1, -1)
        features = np.array([year, adultmortality, alcohol, bmi, polio, diphtheria, hivaids, gdp]).reshape(1, -1)
        prediction = model.predict(features)

        return render_template('index.html', lifeExpectancy=prediction[0])


if __name__ == '__main__':
    app.run(debug=True)
