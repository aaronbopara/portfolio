# Logisitical Regression
# Here we are using the health_report.csv file located in the repository

# Imports (some require pip installs)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import f1_score, ConfusionMatrixDisplay, roc_auc_score, roc_curve

# Load data
filepath = r'../data/health_report.csv'
health_df = pd.read_csv(filepath)
health_df.head()

# First, feature engineer column BMI
health_df['BMI'] = (health_df['Weight']*10000)/(health_df['Height']**2)

# With Seaborn, visualise BMI vs IsHealthy in the form of a Scatterplot
hue_colours = {0:'#FF8181', 1: '#67B587'}
g = sns.scatterplot(x = 'BMI', y = 'IsHealthy', data = health_df, color = '#67B587', hue = 'IsHealthy', palette=hue_colours)
g.set_title('BMI - Health Scatterplot')
sns.despine()
plt.show()

# From the visualisation, we can conclude that 
# the relationship between health status and BMI is non-linear
# Healthy individuals are associated with a BMI within the range 18.5 - 25

# Feature Selection and Train/Test Split
X = health_df[['BMI']]
y = health_df['IsHealthy']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=123)

# Initialise a Logistic Regression Model
model = DecisionTreeClassifier(max_depth=3)

# Fit Model to Training Data
model.fit(X_train, y_train)

# Make Predictions on Test Data
y_pred = model.predict(X_test)

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

# Plot the Decision Tree to explore conditions
fig, ax = plt.subplots(figsize = (16,16))
plot_tree(model, ax=ax)
plt.show()

# Conclusion: Our Decision Tree is a Perfect Classifier with all metrics scoring 1
# There are no misclassifications (neither FP nor FN)
# This confirms our initial observation that BMI and Health have a non-linear relationship
