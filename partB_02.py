from numpy.random import RandomState
import pandas as pd

df = pd.read_csv('classification.csv')
rng = RandomState()

train_data = df.sample(frac=0.8,random_state=rng)
test_data = df.loc[~df.index.isin(train_data.index)]

print(test_data)