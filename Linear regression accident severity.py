import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample synthetic data creation (if you have a CSV, use pd.read_csv)
data = {
    'Accident_Severity': [1, 2, 1, 3, 2, 1, 2, 3, 1, 2],
    'Number_of_Vehicles': [2, 3, 1, 4, 2, 1, 3, 5, 2, 3],
    'Number_of_Casualties': [1, 2, 1, 3, 2, 1, 2, 4, 1, 2],
    'Weather_Conditions': ['Clear', 'Rain', 'Clear', 'Fog', 'Clear', 'Rain', 'Rain', 'Fog', 'Clear', 'Rain'],
    'Road_Surface_Conditions': ['Dry', 'Wet', 'Dry', 'Wet', 'Dry', 'Wet', 'Wet', 'Wet', 'Dry', 'Wet'],
    'Light_Conditions': ['Daylight', 'Darkness', 'Daylight', 'Darkness', 'Daylight', 'Daylight', 'Darkness', 'Darkness', 'Daylight', 'Darkness'],
    'Speed_Limit': [30, 40, 30, 50, 30, 30, 40, 60, 30, 40],
    'Urban_or_Rural_Area': ['Urban', 'Rural', 'Urban', 'Rural', 'Urban', 'Urban', 'Rural', 'Rural', 'Urban', 'Rural']
}
df = pd.DataFrame(data)

# Encode categorical variables
df_encoded = pd.get_dummies(df.drop('Accident_Severity', axis=1), drop_first=True)

# Prepare features (X) and target (y)
X = df_encoded
y = df['Accident_Severity']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model definition and training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Mean squared error:", mean_squared_error(y_test, y_pred))
print("R2 score:", r2_score(y_test, y_pred))

# Show sample predictions
pred_df = X_test.copy()
pred_df['Actual_Severity'] = y_test
pred_df['Predicted_Severity'] = y_pred.round(2)
print(pred_df)
