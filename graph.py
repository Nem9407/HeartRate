import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('result/cdata.csv', header=None, names=['date', 'rate'])
df.plot()
plt.show()