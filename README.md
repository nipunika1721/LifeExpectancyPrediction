
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

1. Country: Select the country for which you want to predict life expectancy.
2. Year: Enter the year for which you want to make the prediction.
3. Status: Select the status of the country (developed or developing).
4. Adult Mortality: Enter the adult mortality rate.
5. Alcohol: Enter the alcohol consumption rate.
6. BMI: Enter the Body Mass Index (BMI).
7. Polio: Enter the polio immunization coverage rate.
8. Diphtheria: Enter the diphtheria immunization coverage rate.
9. HIV/AIDS: Enter the estimated HIV/AIDS prevalence rate.
10. GDP: Enter the Gross Domestic Product (GDP) per capita.

# Example

 For example, you can input the following values:

1. Country: Afghanistan
2. Year: 2015
3. Status: Developing
4. Adult Mortality: 263.0
5. Alcohol: 0.01
6. BMI: 19.1
7. Polio: 6.0
8. Diphtheria: 65.0
9. HIV/AIDS: 0.1
10. GDP: 584.259210

After clicking the "Predict" button, you should see the predicted life expectancy for the given input.
