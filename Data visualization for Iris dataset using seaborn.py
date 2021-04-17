#import libraries
import numpy as np
import pandas as pd
import seaborn as sns

#apply the deafault theme
sns.set_theme()
#load an example dataset
df=sns.load_dataset('iris')
print(df)

df_sepal_length=df['sepal_length']
df_petal_length=df['petal_length']
sns.displot(df_sepal_length,bins=5)

sns.jointplot(data=df_sepal_length,kind='reg')

sns.color_palette('Spectral',as_cmap=True)
sns.jointplot(data=df_sepal_length,kind='reg',height=4)

sns.color_palette('Spectral',as_cmap=True)
sns.jointplot(data=df_sepal_length,kind='kde')

import seaborn as sns
sns.kdeplot(df_sepal_length)

sns.color_palette('Spectral',as_cmap=True)
sns.pairplot(df,hue='species')

sns.barplot(df.values[:,3])

sns.set_theme(style='whitegrid')
tips=sns.load_dataset('tips')
ax=sns.barplot(x='day',y='total_bill',data=tips)

ax=sns.barplot(data=df)

ax=sns.barplot(data=df,estimator=np.cov)

sns.countplot(data=df)

sns.boxplot(data=df)

sns.violinplot(data=df)

sns.stripplot(data=df)

sns.violinplot(data=df)

sns.swarmplot(data=df)

sns.swarmplot(data=df,color='red')

df_cov=df.cov()
ax=sns.heatmap(df_cov)