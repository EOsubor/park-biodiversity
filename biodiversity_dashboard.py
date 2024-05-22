import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the merged DataFrame
merged_df = pd.read_csv('merged_df.csv')

# Set page title
st.set_page_config(page_title='Biodiversity Dashboard')

# Add a title and description
st.title('Biodiversity in National Parks')
st.write('Explore the biodiversity data and analyze endangered species in national parks.')

# Display the merged DataFrame
st.subheader('Merged Data')
st.write(merged_df)

# Display the correlation analysis
endangered_species = merged_df[merged_df['conservation_status'] == 'Endangered']
correlation = endangered_species['observations'].corr(endangered_species['conservation_status'].apply(lambda x: 1 if x == 'Endangered' else 0))
st.subheader('Correlation Analysis')
st.write(f"Correlation between number of observations and endangered status: {correlation:.2f}")

# Display the scatter plot
st.subheader('Scatter Plot')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=endangered_species, x='observations', y='conservation_status', alpha=0.7)
plt.xlabel('Number of Observations')
plt.ylabel('Endangered Status')
plt.title('Relationship between Observations and Endangered Status')
st.pyplot(fig)