# Unsupervised Machine Learning 
 
# Here we are using the mall_customers.csv file located in the repository
# Here we will explore the distrubtion of clients across two of their features - Income and Spending Score 
# The main task is to find the optimal number of clusters and group individuals 
# according to their similarities, to inform the Mall owners od the types of customers that visit their 
# facilities. This will help to form a strategy in terms of what shops to open, so they 
# fit the client profile of the shoppers.

# Imports (some require pip installs)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

# Load Data
df = pd.read_csv(r'../data/mall_customers.csv')
df.head()

# Data exploration 
# First, always check for missing data (even if the task doesn't ask for it explicitly)
df.info()

# Next, visualise the distribution of Income across clients
g = sns.histplot(x = 'Income', data = df, color = '#7EABAD')
g.set_title('Client Distribution by Income')
sns.despine()
plt.show()

# Do the same for Spending Score
g = sns.histplot(x = 'Spending_Score', data = df, color = '#7EABAD')
g.set_title('Client Distribution by Spending')
sns.despine()
plt.show()

# Lastly, visualise a Scatter Plot to see the distribution of clients across both features
g = sns.scatterplot(x = 'Income', y= 'Spending_Score', data = df, color ='#7EABAD')
g.set_title('Income vs Spending - Scatterplot')
sns.despine()
plt.show()

# Conclusion:
# From the scatterplot we can largely spot 5 areas with high concentration of customers
# It seems like people in the lower and upper range of their incomes both exhibit two types of behaviours
# people who spend a lot and people who spend little
# People with average income and the only ones who largely spend moderately and
# don't fall in either of the extreme spending cases
# Initial proposition - 5 clusters

#Finding the optimal split with a Silhouette Analysis

# Create a container for the Silhouette Scores
km_sil = []

# Iterate over a range of clusters - e.g. from 2 to 10
# On each iteration fit a model and append its inertia to the container
# Note - for a Silhouette Analysis we require at least 2 clusters
for k in range(2,11):
    km = KMeans(n_clusters=k, n_init = 'auto')
    km.fit(X)
    y_pred = km.predict(X)
    km_sil.append(silhouette_score(X,y_pred))

# Plot the number of clusters against the silhouette score to identify optimal k
x = np.arange(2,11)
g = sns.lineplot(x=x, y = km_sil, color = '#7EABAD')
g.set_title('Income vs Spending - Silhouette Score')
sns.despine()
plt.show()


# Silhouette Score across Samples

# Select the data for the Clustering
X = df[['Income', 'Spending_Score']]

# Initialise the K-Means model with 5 clusters
km = KMeans(n_clusters = 5, n_init = 'auto')

# Fit and predict
km.fit(X)
y_pred = km.predict(X)

# Store features and predictions in a single dataframe
cluster_df = X.copy()
cluster_df['cluster'] = y_pred

# Plot the Scatter Plot for 5 clusters
hue_colours = {2:'#FF7C80', 0: '#72F7AE', 1:'#7EABAD', 3: 'red', 4:'black'}
g = sns.scatterplot(x = 'Income', y= 'Spending_Score', data = cluster_df, hue = 'cluster', palette=hue_colours)
g.set_title('Spending vs Income - 5-Cluster K-Means')
sns.despine()
plt.show()

# Use predictions to feed into silhouette_samples() function
sample_silhouette_values = silhouette_samples(X,y_pred)

# Concatenate predicted clusters with their silhouette scores per sample
sil_df = pd.DataFrame({'cluster':y_pred, 'sil_score':sample_silhouette_values})
sil_df.head()

# A little data preparation for the Silhouette Plot
# First, let's sort our observations per cluster and silhouette score
sil_df.sort_values(['cluster', 'sil_score'], inplace=True)

# Next, let's reset the index and import it, so that the index increases in the same order as cluster and sil_score
sil_df.reset_index(inplace=True, drop=True)
sil_df.reset_index(inplace=True)

# For the visual, we can also use the model silhouette score (to compare observations against the average)
sil_avg = silhouette_score(X,y_pred)

# Lastly, visualise the Silhouette Plot on Sample level for all 500 observations
fig, ax = plt.subplots(figsize = (12,8))    # Customise the size of the visual
hue_colours = {2:'#FF7C80', 0: '#72F7AE', 1:'#7EABAD', 3: 'red', 4:'black'}
g = sns.barplot(x = 'sil_score', y = 'index', data = sil_df, hue = 'cluster', orient = 'h', ax = ax, palette = hue_colours)
plt.axvline(x=sil_avg, c='black', label = "Average Silhouette Score", linestyle = 'dashed')
g.set_title('Silhouette Analysis - 5 Clusters')
sns.despine(left = True)
ax.set_yticks([])
plt.legend()
plt.show()
