from sklearn.metrics import roc_auc_score

def evaluate_model(train_data, test_data):
    # takes as input train and test dataframe where model predictions have been added
    # evaluates the model based on roc_auc_score of training and test data 
    # prints each score
    roc_auc_train = roc_auc_score(train_data['diabetes_mellitus'], train_data['predictions'])
    roc_auc_test = roc_auc_score(test_data['diabetes_mellitus'], test_data['predictions'])
    print(f"Train ROC AUC: {roc_auc_train}")
    print(f"Test ROC AUC: {roc_auc_test}")