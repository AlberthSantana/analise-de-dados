import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

plt.figure(figsize= (6, 8))

sns.histplot(data= titanic, x = 'age')

plt.show()

print(titanic)