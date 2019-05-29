import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

def check_validation_set(train_set, validation_set) -> bool:
    """
        https://towardsdatascience.com/using-random-forest-to-tell-if-you-have-a-representative-validation-set-4b58414267f6
    """
    # Create the new target
    train_set['train'] = 1
    validation_set['train'] = 0
    # Concatenate the two datasets
    train_validation = pd.concat([train_set, validation_set], axis=0)
    # Split up the dependent and independent variables
    X_train = train_validation.drop('train', axis=1)
    y_train = train_validation['train']
    # Set up the model
    rfc = RandomForestClassifier(n_estimators=10, random_state=1)
    # Run cross validation
    cv_results = cross_val_score(rfc, X_train, y_train, cv=5, scoring='roc_auc')
    print(cv_results)
    mean_result = np.mean(cv_results)
    print(mean_result)
    if mean_result >= 0.5:
        return True
    return False
