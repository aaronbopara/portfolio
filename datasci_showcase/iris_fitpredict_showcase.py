# Knn with test and train/fit and predict workflow
# Here we are using the iris dataset from scikit learn 

# Imports (some are pip installed)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load Iris Bunch object
iris = load_iris()

 # Load feature dataframe X
X = pd.DataFrame(data = iris.data, columns = iris.feature_names)
display(X)

# Load target series y
y = pd.Series(data = iris.target)
display(y)

# Conctenate:
iris_df = X.copy()
iris_df['class'] = y
iris_df.head()

# Explore the data by creating a scatterplot 
hue_colours = {0:'#67B587', 1: '#FF8181', 2: '#35E0C1'}
g = sns.scatterplot(x = 'petal length (cm)', y = 'petal width (cm)', data = iris_df, hue = 'class', palette=hue_colours)
g.set_title('Iris Distribution by Petal Length vs Width')
sns.despine()
plt.show()

# We can see that class 0 - Setosa, is the most clearly pronounced group of observations
# class 1 - Versicolor, and class 2 - Virginica, are closer to one another in terms of Petal features,
# yet there is still a clear separation between the two
# however, class 1 and 2 are quite mixed up when it comes to Sepal Features

# Here we perform some classification on the data using scikit learn

# Split X and y into Train and Test sets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 123)

# Initialise an instance of a KNN Classifier model
knn = KNeighborsClassifier()

# Fit the model to X_train and y_train
knn.fit(X_train, y_train)

# With the trained model, make predictions on X_test - store in y_pred
y_pred = knn.predict(X_test)

# Calculate model accuracy score on the test data
acc_knn = accuracy_score(y_test, y_pred)
print(f'Accuracy Score for KNN: {acc_knn}')

# We can then use the objects created above to visualise the correct predictions 
test_df = X_test.copy()
test_df['class'] = y_test
test_df['class pred'] = y_pred

test_df.reset_index(inplace = True)
test_df = test_df[['index', 'class', 'class pred']]
test_df.head()

# Create a Grid with 'class' on the index, 'class pred' as column labels, count of 'index' as value.
# Here we can see that out of 30 classifications 29 were correctly classified. 
test_grid = pd.crosstab(test_df['class'], test_df['class pred'], values = test_df['index'], aggfunc = 'count')
display(test_grid)

# We can also create a heatmap which visualises the grid
sns.heatmap(test_grid, annot = True, cmap = 'BuGn', linewidths=0.5)
plt.show()

# This means that the proportion of correct classifications is 29/30 = 96.67, which is also the accuracy score