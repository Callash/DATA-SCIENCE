import pandas as pd

# Example input as a DataFrame (using the same column encoding as the model)
sample_input = pd.DataFrame([{
    'Number_of_Vehicles': 3,
    'Number_of_Casualties': 2,
    'Speed_Limit': 40,
    # One-hot encoding for categorical variables (set to 1 if matches, else 0)
    'Weather_Conditions_Rain': 1,
    'Weather_Conditions_Fog': 0,
    'Road_Surface_Conditions_Wet': 1,
    'Light_Conditions_Darkness': 1,
    'Urban_or_Rural_Area_Rural': 1,
}])

# Ensure all columns match the training data (add missing columns as 0)
for col in model.feature_names_in_:
    if col not in sample_input:
        sample_input[col] = 0
sample_input = sample_input[model.feature_names_in_]

# Predict severity
predicted_severity = model.predict(sample_input)
print(f"Predicted Accident Severity: {predicted_severity[0]:.2f}")
