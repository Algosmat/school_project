import pandas as pd

data = pd.read_csv("classification.csv")

df = pd.DataFrame(data, columns=['X1','X2'])

summmary_of_data = df.describe()

print(summmary_of_data)