from sklearn.ensemble import RandomForestClassifier
from numpy.random import RandomState
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

raw_data = pd.read_csv('classificationTrue.csv')
df = pd.DataFrame(raw_data)
X = df[['X1','X2']]
y = df['Group']


x_train, x_test,y_train,y_test = train_test_split(X,y, test_size=.2,random_state=0)
pipe = Pipeline([('classifier' , RandomForestClassifier())])
clf = LogisticRegression()
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)
print(classification_report(y_test,y_pred))


