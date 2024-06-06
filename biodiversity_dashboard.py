import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
observations = pd.read_csv('observations.csv')
species_info = pd.read_csv('species_info.csv')

# Merge the dataframes
merged_df = pd.merge(observations, species_info, on='scientific_name')

# Fill NaN values in 'conservation_status' with 'Not Listed'
merged_df['conservation_status'].fillna('Not Listed', inplace=True)

# Display the merged dataframe in the app
st.write("Merged DataFrame")
st.write(merged_df.head())

# Interactive filters
selected_category = st.selectbox("Select Category", options=merged_df['category'].unique())
selected_park = st.selectbox("Select Park", options=merged_df['park_name'].unique())

filtered_df = merged_df[(merged_df['category'] == selected_category) & (merged_df['park_name'] == selected_park)]

# Slider for number of observations
observation_threshold = st.slider("Minimum number of observations", min_value=0, max_value=int(filtered_df['observations'].max()), value=10)
filtered_df = filtered_df[filtered_df['observations'] >= observation_threshold]

st.write(f"Filtered DataFrame with Category: {selected_category}, Park: {selected_park}, Observations >= {observation_threshold}")
st.write(filtered_df.head())

# Feature Engineering
# Convert categorical features to numerical values using one-hot encoding
filtered_df = pd.get_dummies(filtered_df, columns=['category', 'park_name'], drop_first=True)

# Define feature columns
feature_columns = [col for col in filtered_df.columns if col not in ['scientific_name', 'common_names', 'conservation_status']]

X = filtered_df[feature_columns]

# Logistic Regression for Threatened Species
y_threatened = filtered_df['conservation_status'] == 'Threatened'  # Target variable for threatened species

# Split the data into training and testing sets for threatened species
X_train_threatened, X_test_threatened, y_train_threatened, y_test_threatened = train_test_split(X, y_threatened, test_size=0.2, random_state=42)

# Create and train the logistic regression model for threatened species
model_threatened = LogisticRegression(max_iter=1000)
model_threatened.fit(X_train_threatened, y_train_threatened)

# Make predictions on the test set for threatened species
y_pred_threatened = model_threatened.predict(X_test_threatened)

# Display the classification report for threatened species
st.write("Logistic Regression Results for Threatened Species")
st.text(classification_report(y_test_threatened, y_pred_threatened))

# Confusion matrix for threatened species
conf_matrix_threatened = confusion_matrix(y_test_threatened, y_pred_threatened)
fig, ax = plt.subplots()
sns.heatmap(conf_matrix_threatened, annot=True, fmt='d', cmap='Blues', ax=ax)
ax.set_title('Confusion Matrix for Threatened Species')
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')
st.pyplot(fig)

# Logistic Regression for Species of Concern
y_concern = filtered_df['conservation_status'] == 'Species of Concern'  # Target variable for species of concern

# Split the data into training and testing sets for species of concern
X_train_concern, X_test_concern, y_train_concern, y_test_concern = train_test_split(X, y_concern, test_size=0.2, random_state=42)

# Create and train the logistic regression model for species of concern
model_concern = LogisticRegression(max_iter=1000)
model_concern.fit(X_train_concern, y_train_concern)

# Make predictions on the test set for species of concern
y_pred_concern = model_concern.predict(X_test_concern)

# Display the classification report for species of concern
st.write("Logistic Regression Results for Species of Concern")
st.text(classification_report(y_test_concern, y_pred_concern))

# Confusion matrix for species of concern
conf_matrix_concern = confusion_matrix(y_test_concern, y_pred_concern)
fig, ax = plt.subplots()
sns.heatmap(conf_matrix_concern, annot=True, fmt='d', cmap='Greens', ax=ax)
ax.set_title('Confusion Matrix for Species of Concern')
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')
st.pyplot(fig)
