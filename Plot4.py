#plot age
plt.figure(figsize=(5, 5))
sns.histplot(x='Age', data=df_analysis)
plt.title('Age in df_analysis')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()