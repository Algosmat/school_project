import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



raw_data = pd.read_csv(r'london_pollution.csv')

df = pd.DataFrame(raw_data, columns=['Date','Bloomsbury','Barking'])


df.set_index('Date').plot()


plt.show()

sns.heatmap(df.isnull(), cbar=False)
plt.show()

