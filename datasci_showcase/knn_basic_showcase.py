# Knn basics 
# Here we are using the heigh_weight_class.csv file, in order to predict an individuals 
# sex using their height and weight 

# Imports 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
filepath = r'../data/height_weight_class.csv'
df = pd.read_csv(filepath)

# Take a peak at the data
df.head()
df.tail()
df.shape
df.info()
df['gender'].value_counts()

# We can visualise the distribution of observations in the form of a Scatterplot

hue_colours = {0:'#67B587', 1: '#FF8181'}
g = sns.scatterplot(x = 'weight', y = 'height', data = df, hue = 'gender', palette = hue_colours)
g.set_title('Height vs Weight - Scatter Plot')
sns.despine()
plt.show()

# Initialise an instance of a KNN Classifier model
knn = KNeighborsClassifier()

# fit the model to the available input-output data
knn.fit(df[['height', 'weight']], df['gender'])

# Construct a new dataframe, unseen by the model

# Aim - make predictions about the gender of each observation in new_df

data = {'height':[185.3425, 155.7853, 168.9043, 192.8832],
        'weight':[92.1123, 56.7865, 62.0043, 102.5543]}
new_df = pd.DataFrame(data)

display(new_df)

prediction = knn.predict(new_df)
print(prediction)