import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

df_by_sex = titanic.groupby('sex')['survived'].sum().reset_index()

plt.figure(figsize=(6, 8))

sns.barplot(data=df_by_sex, x = 'sex', y = 'survived')

plt.show()