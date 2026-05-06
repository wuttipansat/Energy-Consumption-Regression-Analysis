# Energy Consumption Regression Analysis

This project analyzes and develops Machine Learning models to predict hourly 'EnergyConsumption'. The prediction uses weather conditions, building area, occupancy, HVAC usage, lighting usage, renewable energy, and time-based features.

## Project workflow

1. Importing the dataset
2. Inspecting the data and checking for missing values
3. Creating time-based features such as day of week, hour, and month
4. Exploring data relationships through visualizations.
5. Creating lag and rolling features for time series modeling
6. Training and comparing multiple regression models
7. Evaluating model performance using MAE, RMSE and R2 Score

## Models

This project compares several regression models includes:

- Ridge Regression
- Lasso Regression
- ElasticNet
- Decision Tree Regressor
- Random Forest Regressor
- Extra Trees Regressor
- Gradient Boosting Regressor
- HistGradientBoosting Regressor
- Support Vector Regressor

### Best Result
    Lasso Regression Model with RMSE: 5.5407

## Getting Started

Install the required dependencies:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn joblib jupyter
```

## Author

Developed by Wuttipan Satienpaisan
