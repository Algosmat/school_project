import numpy as np
from numpy.random import RandomState
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.metrics import classification_report

raw_data = pd.read_csv('classificationTrue.csv')
df = pd.DataFrame(raw_data)
X = df[['X1','X2']]
y = df['Group']


x_train, x_test,y_train,y_test = train_test_split(X,y, test_size=.2,random_state=0)

model = KNeighborsClassifier(n_neighbors=25)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(classification_report(y_test, y_pred))