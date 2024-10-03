#plot semester 1 grades
plt.figure(figsize=(5, 5))
sns.histplot(x='Semester1Grade', data=df_analysis)
plt.title('Grades in df_analysis')
plt.xlabel('grades')
plt.ylabel('Count')
plt.show()