# Logisitical Regression
# Here we are using the health_report.csv file located in the repository

# Imports (some require pip installs)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler, StandardScaler, OneHotEncoder, Binarizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import f1_score, ConfusionMatrixDisplay, roc_auc_score, roc_curve

# Here we will take the health_df dataframe and train a logistical regression model
# This will classify 'IsMale' and 'Height' following all stages of a fit-predict workflow

# Load data
filepath = r'../data/health_report.csv'
health_df = pd.read_csv(filepath)
health_df.head()

# Feature Selection and Train-Test Split
X = health_df[['Height']]
y = health_df['IsMale']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=123)

# Initialise a Logistic Regression Model
model = LogisticRegression()

# Fit Model to Train Data
model.fit(X_train, y_train)

# Test model on Test Data
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)      # this is a 2D array, which we can store in a DF
y_pred_proba_df = pd.DataFrame(y_pred_proba)    # Create a DataFrame with produced probabilities

# Evaluate performance
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

# Plot Confusion Matrix
fig, ax = plt.subplots()
g=ConfusionMatrixDisplay.from_predictions( y_test, y_pred, ax = ax, cmap = 'BuGn')

# Plot ROC Curve to Visualise
fpr, tpr, thresh = roc_curve(y_test, y_pred_proba_df[1])

g = sns.lineplot(x = fpr, y= tpr, color = '#67B587')
g.set_title('ROC - AUC')
sns.despine()
plt.show()