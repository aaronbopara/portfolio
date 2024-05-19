# Random Forest 
# Here we are using the titanic.csv file located in the repository
# Here we will build a predictive model, which can identify which passengers are most at 
# risk of not surviving the disaster. 

# Imports (some require pip installs)
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import f1_score, ConfusionMatrixDisplay, roc_auc_score, roc_curve
from sklearn.model_selection import GridSearchCV

# Data Load
filename = r'../data/titanic.csv'
titanic_df = pd.read_csv(filename)

# Data Cleaning and Encoding of Categorical Features

titanic_df.dropna(axis = 0, inplace=True)
titanic_df['Sex'] = titanic_df['Sex'].map({'female':1, 'male':0})
titanic_df['Embarked'] = titanic_df['Embarked'].map({'S':0, 'C':1, 'Q':2})
titanic_df.head()

# Feature Selection and Train/Test split

X = titanic_df[['Age', 'Fare', 'Pclass', 'Sex', 'Embarked']]
y = titanic_df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=123)

# Initialise Random Forest Classifier
clf = RandomForestClassifier()

# Hyperparameter Tuning
parameters = {'max_depth':        [2,3,4,5,6,7,8,9,10],
              'min_samples_leaf': [5, 10, 20],
              'n_estimators':[25,50,100,150]}  

model = GridSearchCV(estimator = clf, param_grid = parameters, cv=5, scoring = 'recall')

# Fit and Predict
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate model performance
acc = accuracy_score(y_test,y_pred)
pr = precision_score(y_test, y_pred)
re = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)

print(f'ROC AUC is {roc_auc}')
print(f'F1 score is {f1}')
print(f'Recall is {re}')
print(f'Precision is {pr}')
print(f'Accuracy Score: {acc:.4f}')