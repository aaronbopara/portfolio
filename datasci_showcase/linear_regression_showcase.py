# Linear Regression
# Here we are using the insurance_v1.csv file located in the repository

# Imports (some require pip installs)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

# We will calculate the correlations between the numerical columns in the data
# and then visualise it with seaborn. 
# We will explore the relationship between the numerical data and the charges per customer 

# Load dataset
filepath = r'../data/insurance_v1.csv'
df = pd.read_csv(filepath)

# Take a peak at the data
df.head()

# Select only the numerical variables in the dataset
# and calculate their correlations
num_df = df[['age', 'children', 'height', 'weight', 'charges']]
num_corr_df = num_df.corr()

# Plot the correlations in the form of a heatmap 
sns.heatmap(num_corr_df, annot = True, cmap = 'BuGn', linewidths=0.5)
plt.show()

# Column charges has the highest correlation with age, followed by weight
# Nevertheless the magnitude of these correlations is too small to claim significance
# Correlation between charges and children or height is pretty much 0
# All of this suggests that these features don't perform well in explaining the target column 'charges'

# Next we will build a linear regression which will predcit medical charges, using only numerical variables. 
# We will also report on regression performance metrics 

# Split data into features and target
X = df[['age', 'height', 'weight', 'children']]
y = df['charges']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=123)

# Create a linear regression model
model = LinearRegression()

# Fit model
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

# Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Report on the evaluation metrics
print(f'MSE is {mse:.4f}')
print(f'RMSE is {mse**0.5:.4f}')
print(f'MAE is {mae:.4f}')
print(f'R-squared is {r2:.4f}')

# Interpretation
# Our model doesn't perform very well - with a RMSE of 11923, our predictions are on average
# more than 10k away from the true medical charge
# the coefficient of determination is positive but very close to zero, indicating that
# our current model is only marginally better than a constant prediction of the average charge in the train dataset