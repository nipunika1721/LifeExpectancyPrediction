
# Life Expectancy Prediction Web Application

This Flask web application predicts life expectancy based on various input features. It utilizes a trained machine learning model to make predictions.

# Prerequisites
Before running the application, ensure you have the following installed:

Python 3.x
Flask
Pandas
NumPy
Joblib

# Installation
1. Clone this repository to your local machine:
    git clone https://github.com/your-username/your-repository.git

2. Navigate into the project directory:
    cd your-repository

3. Install the required dependencies:
   pip install -r requirements.txt

# Usage

* Ensure you are in the project directory.
* Run the Flask application:
  python app.py
* Open your web browser and go to http://127.0.0.1:5000/
* You should see the home page of the application. Enter the required information and click the "Predict" button to get the predicted life expectancy.

# Input Features

Country: Select the country for which you want to predict life expectancy.
Year: Enter the year for which you want to make the prediction.
Status: Select the status of the country (developed or developing).
Adult Mortality: Enter the adult mortality rate.
Alcohol: Enter the alcohol consumption rate.
BMI: Enter the Body Mass Index (BMI).
Polio: Enter the polio immunization coverage rate.
Diphtheria: Enter the diphtheria immunization coverage rate.
HIV/AIDS: Enter the estimated HIV/AIDS prevalence rate.
GDP: Enter the Gross Domestic Product (GDP) per capita.

# Example

 For example, you can input the following values:

Country: Afghanistan
Year: 2015
Status: Developing
Adult Mortality: 263.0
Alcohol: 0.01
BMI: 19.1
Polio: 6.0
Diphtheria: 65.0
HIV/AIDS: 0.1
GDP: 584.259210

After clicking the "Predict" button, you should see the predicted life expectancy for the given input.
