import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import GridSearchCV
import eli5
from eli5.sklearn import PermutationImportance

data_file = 'heart_cleveland_upload.csv'

## Preparation
# Read data
data = pd.read_csv(data_file)
print(data.head())
data.info()

# Prepare data, divide attributes

# Clean , Split data
data=data.dropna()
x=data.drop(labels=['condition'],axis=1)
y=data['condition']

x_train, x_val, y_train, y_val = train_test_split(x,y,test_size=0.3)
plt.figure(figsize=(12,5))
sns.heatmap(data.corr(),annot=True)
plt.show()


## Model
rf_model = RandomForestClassifier()

# Create the parameter grid based on the results of random search
group_param = {
    'max_depth': [2,4,6],
    'min_samples_leaf': [3,5],
    'n_estimators': [100,200],
    'oob_score': [True],
    'random_state': [0],
}

# Instantiate the grid search model
hyperp_srch = GridSearchCV(estimator = rf_model, param_grid = group_param,
                      cv = 5, return_train_score=False)

hyperp_srch.fit(x_train, y_train)
#print(hyperp_srch.best_params_)
best_hyper = hyperp_srch.best_estimator_
rf_model = RandomForestClassifier(**best_hyper.get_params())
rf_model.fit(x_train, y_train)

y_pred_train=rf_model.predict(x_train)
y_pred_val=rf_model.predict(x_val)


## End
print('Classification Report: \n')
print(classification_report(y_val,y_pred_val))
print('\nConfusion Matrix: \n')
print(confusion_matrix(y_val,y_pred_val))

permutation = PermutationImportance(rf_model, random_state=2).fit(x_train, y_train)
eli5.explain_weights(permutation  , feature_names = x.columns.tolist())
print(eli5.format_as_text(eli5.explain_weights(permutation, feature_names = x.columns.tolist())))
