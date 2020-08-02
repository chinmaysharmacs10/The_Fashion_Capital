import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('amazon_tshirts_new.csv')

data.rename(columns={'Tshirt_no_of_ratings':'Number_of_ratings','Tshirt_cstmr_rating_name':'Customer_rating','Tshirt_cstmr_rating_cstmr_review':'Customer_Review','Tshirt_cstmr_rating_date':'Review_date'},inplace=True)
data['Review_date'] = data['Review_date'].str[21:]
data['Review_date'] = pd.to_datetime(data['Review_date'])
data['Review_date'] = data['Review_date'].dt.strftime('%Y%m%d')

data['Tshirt_name'] = data.Tshirt_name.astype(str)
data['Review_date'] = data.Review_date.astype(str)
data['Customer_rating'] = data.Customer_rating.astype(str)

data['Customer_rating'] = data['Customer_rating'].str[:3]
data['Customer_rating'] = pd.to_numeric(data['Customer_rating'])
data.Review_date = pd.to_numeric(data.Review_date,errors='coerce')
data['Number_of_ratings'] = data['Number_of_ratings'].str.replace(',','').astype(int)
data = data.dropna()

plt.scatter(data['Customer_rating'],data['Review_date'])
plt.xlabel('Customer_rating')
plt.ylabel('Review_date')
plt.show()

X = pd.DataFrame()
X['rating']= data['Customer_rating']
X['date'] = data['Review_date']
X1 = X.to_numpy()

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score



kmeans = KMeans(n_clusters=2,init='k-means++',random_state=0).fit(X1)
centers = kmeans.cluster_centers_
labels = kmeans.predict(X1)

accuracy = silhouette_score(X,labels)
print(accuracy)

plt.scatter(X1[labels==0,0],X1[labels==0,1],s=100,c='red',label='Cluster1')
plt.scatter(X1[labels==1,0],X1[labels==1,1],s=100,c='blue',label='Cluster2')
plt.show()

cluster_map = pd.DataFrame()
cluster_map['data_index'] = X.index.values
cluster_map['cluster'] = labels

import pickle
model = {'model':KMeans}
pickle.dump(model,open('KMeans_pickle'+".p","wb"))