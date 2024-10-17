#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# Load the datasets
combined_data = pd.read_csv('Combined_Data[1].csv')
mental_health_data = pd.read_csv('Mental_Health_Dataset[2].csv')

#  add a unique index column if there is none
# This will serve as a common key for joining
combined_data['id'] = combined_data.index
mental_health_data['id'] = mental_health_data.index

# Perform a left join
merged_data = pd.merge(combined_data, mental_health_data, how='left', on='id')

# Save the merged dataset to a new CSV file
merged_data.to_csv('dataset.csv', index=False)

print("Left join completed and saved as 'dataset.csv'")


# In[5]:


import pandas as pd

# Load the newly created dataset
new_data = pd.read_csv('dataset.csv')

# Display the first 5 rows of the dataset
print(new_data.head())


# In[8]:


import pandas as pd
import os

# File path
combined_data_path = 'Combined_Data[1].csv'  # Assuming this file is in the current directory
mental_health_data_path = 'Mental_Health_Dataset[2].csv'  # Assuming this file is in the current directory

# Load datasets
combined_data = pd.read_csv(combined_data_path)
mental_health_data = pd.read_csv(mental_health_data_path)

# Get sizes in MB
combined_data_size = os.path.getsize(combined_data_path) / (1024 * 1024)  # Size in MB
mental_health_data_size = os.path.getsize(mental_health_data_path) / (1024 * 1024)  # Size in MB

# Get the number of records (rows)
combined_data_records = combined_data.shape[0]  # Number of rows in Combined Data
mental_health_data_records = mental_health_data.shape[0]  # Number of rows in Mental Health Data

# Print sizes and number of records
print(f"Size of Combined Data: {combined_data_size:.2f} MB, Number of Records: {combined_data_records}")
print(f"Size of Mental Health Dataset: {mental_health_data_size:.2f} MB, Number of Records: {mental_health_data_records}")


# # day_1 code for preprocessing of the dataset
# 

# In[2]:


import pandas as pd

# Load the dataset
data = pd.read_csv('dataset.csv')

# Displaying the first few rows of the dataset
print(data.head())

# obtainig the summary of the dataset, including data types and non-null values
print(data.info())

# Check for missing values in each column
print(data.isnull().sum())

# Get the unique values for each column to understand their structure
for column in data.columns:
    print(f"Unique values in '{column}':\n{data[column].unique()}\n")


# In[4]:


import pandas as pd

# Loading the dataset
df = pd.read_csv('dataset.csv')

# Dropping irrelevant columns like unnamed, id
df.drop(['Unnamed: 0', 'id'], axis=1, inplace=True)

# Convert 'Timestamp' to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Filling the  missing values in 'statement' with a placeholder
df['statement'].fillna('No statement provided', inplace=True)

# Filling the  missing values in 'self_employed' with a mode (most frequent value)
df['self_employed'].fillna(df['self_employed'].mode()[0], inplace=True)

# Removing the duplicate rows
df.drop_duplicates(inplace=True)

# Checking for any remaining missing values
missing_values = df.isnull().sum()
print("Missing values after preprocessing:\n", missing_values)

# Saving the cleaned data to a new CSV file
df.to_csv('cleaned_dataset.csv', index=False)

# finally done with the preprocessing techniques
print("Data preprocessing completed!")


# In[7]:


pre_process_dataset=pd.read_csv("cleaned_dataset.csv")
pre_process_dataset.head(5)


# In[ ]:




