# MNIST Dataset Machine Learning Project

## Overview
This project utilizes the MNIST dataset to perform machine learning tasks, including clustering and regression. The MNIST dataset consists of a large number of handwritten digits, commonly used for training various image processing systems.

## Libraries Used
The project makes use of the following libraries:
- **NumPy**: For numerical computing and array operations.
- **Pandas**: For data manipulation and analysis.
- **Seaborn**: For data visualization and exploration.
- **Scikit-learn**: For machine learning algorithms and tools.
- **Matplotlib**: For creating visualizations and plots.

## Tasks Performed

### 1. Data Preprocessing
- **Scaling**: The data is scaled using Min-Max and Standard scalers to normalize the feature values.
- **Dimensionality Reduction**: Principal Component Analysis (PCA) is applied for feature reduction.
- **Train-Test Split**: The dataset is split into training and testing sets for model evaluation.

### 2. Clustering
- **K-Means Clustering**: Unsupervised learning algorithm used to group similar digits together.
- **DBSCAN**: Density-based clustering to identify clusters of arbitrary shapes.

### 3. Regression
- **Linear Regression**: Simple regression model to predict numerical values.
- **K-Nearest Neighbors Regression (KNN)**: Algorithm for predicting values based on the nearest data points.
- **Random Forest Regression**: Ensemble learning method for regression tasks.

### 4. Evaluation
- **Metrics**: Various evaluation metrics are used such as Mean Squared Error, Mean Absolute Error, R-squared, and Cross-Validation scores.
- **Visualizations**: Visual representations of the results, including scatter plots, regression plots, and error distributions.

### Methods and Models

- **Random Forest Classifier:** Employed a Random Forest Classifier with 100 decision trees. The model was trained using the `fit()` function and evaluated using metrics such as Root Mean Square Error (RMSE), Mean Absolute Error (MAE), and R-squared (R^2).
- **Logistic Regression, K-Nearest Neighbors (KNN), and Support Vector Machine (SVM):** Tested these classifiers alongside Random Forest, and evaluated their performance metrics such as R^2 and accuracy score.
- **Cross-Validation:** Employed k-cross-validation to assess the robustness of the models. Utilized the `cross_val_score()` function and plotted the results for all models.

### Results and Analysis

| Model                | Precision | Recall | Accuracy Score |
|----------------------|-----------|--------|----------------|
| Logistic Regression  | 0.89      | 0.90   | 0.89           |
| Random Forest        | 0.92      | 0.92   | 0.92           |
| KNN                  | 0.807     | 0.803  | 0.795          |
| SVM                  | 0.87      | 0.86   | 0.87           |

#### Analysis:

- **Data Quality:** No missing values or outliers were found in the datasets.
- **T-SNE Plot Observation:** Identified scattered distribution of digit 2 values in the plot.
- **Model Performance:** Among the tested models, Random Forest Classifier with 100 trees yielded the highest accuracy score of 0.92.
- **Conclusion:** Random Forest Classifier demonstrated superior accuracy and robustness compared to other models, making it the optimal choice for digit prediction tasks.

## Conclusion

In conclusion, the project successfully evaluated various machine learning models for digit recognition using the MNIST dataset. Through meticulous analysis and experimentation, Random Forest Classifier emerged as the top performer, achieving a precision of 0.92. This model can be reliably employed for digit recognition tasks with high accuracy and efficiency.

## Future Work

Future iterations of the project could explore additional feature engineering techniques, hyperparameter tuning, and ensemble methods to further enhance the performance of the models. Moreover, investigating alternative datasets and expanding the scope beyond digit recognition could provide valuable insights into broader pattern recognition tasks.
