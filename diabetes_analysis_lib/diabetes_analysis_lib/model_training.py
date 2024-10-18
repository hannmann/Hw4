from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

def make_predictions(data, features, target):
    # Trains a logistic regression model to predict likelihood of taregt based on the features.
    # Then the function uses the trained model to make predictions for training and test data
    model = LogisticRegression()
    model.fit(data[features], data[target])
    
    # make predictions
    # predictions will be added to the dataframes in column 'predictions'
    data['predictions'] = model.predict_proba(data[features])[:, 1]
    data['predictions'] = model.predict_proba(data[features])[:, 1]

    return data 
    

#def make_predictions(model, scaler, data, features):
    """Generates predictions using the trained model."""
    data[features] = scaler.transform(data[features])
    return model.predict_proba(data[features])[:, 1]


#def make_predictions(model)
## Trainind data
    train_data['predictions'] = model.predict_proba(train_data[features])[:, 1]

## Testing data
    test_data['predictions'] = model.predict_proba(test_data[features])[:, 1]
