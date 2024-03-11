
# Stack Overflow Survey 2020 Salary Prediction Web App

## Overview
This project utilizes the Stack Overflow Survey data from 2020 to predict the salary of software engineers based on various factors such as country, experience level, and education level. The prediction model is built using Python, machine learning techniques, and the Streamlit library for creating interactive web applications.

## Project Structure
The project consists of the following components:

* `Stack_APP_Build`: This directory contains the source code for the salary prediction model and the Streamlit web application.

    - `salary_prediction_model.py`: Python script containing code for building and training the salary prediction model.
    
    - `app.py`: Python script containing code for the Streamlit web application. This script allows users to input their country, experience level, and education level to predict their salary, as well as explore the dataset through various interactive visualizations.

    - `Page_predict.py`: This script allows users to input their country, experience level, and education level to predict their salary.

    - `Page_explore.py`: Explore the dataset through various interactive visualizations. You can scroll the bar chart and line chart also.

## How to Run the Web App
To run the Salary Prediction web app, follow these steps:

1. Clone this repository to your local machine.

2. Navigate to the project directory.

3. Install the required dependencies using the command:

    you can install these dependencies individually:

    Pip install streamlit, pandas, numpy, matplotlib, scikit-learn, pickle

4. Run the Streamlit web application using the command:

        Streamlit run App.py

5. Open a web browser and go to the URL displayed in the terminal to access the web app.


## Usage
Once the web app is running, users can interact with it as follows:

- Input their country, experience level, and education level using the provided dropdown menus.

- Click the "Predict Salary" button to see the predicted salary based on the input.

- Explore the dataset by switching between different tabs in the web app interface, which contain interactive visualizations such as Pie Plot, bar charts, and line Chart.

## Future Improvements
Some potential enhancements for the project include:

- Incorporating additional features from the survey dataset to improve the accuracy of the salary prediction model.

- Implementing more advanced machine learning algorithms and techniques to enhance the model's predictive performance.

- Enhancing the user interface of the web app with additional features and customization options.



