import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    # Loads the dataset from a CSV file."""
    return pd.read_csv(file_path)


def split_data(df, test_size=0.2, random_state=42):
    # Splits the dataset into train and test sets.
    train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
    return train_data, test_data



def clean_data(data):
    # input either training data or test data
    # Remove NaN values from specific columns in the test set
    data.dropna(subset=['age', 'gender', 'ethnicity'], inplace=True)

    # Fill NaN values in height and weight columns with the mean in the test set
    data['height'].fillna(data['height'].mean(), inplace=True)
    data['weight'].fillna(data['weight'].mean(), inplace=True)

    #Generate dummies for ethnicity in the test set
    data = pd.get_dummies(data, columns=['ethnicity'])

    # Create binary variable for gender in the test set
    data['gender'] = data['gender'].map({'M': 1, 'F': 0})

    return data
