# plot gender 1 = male (blue) , 0 = female (pink)
Gender = df_analysis['Gender'].value_counts()
y = np.array(Gender)
plt.pie(y, labels=Gender.index, autopct='%1.1f%%', startangle=140, colors= ["pink","#ADD8E6"])
plt.title('Gender Distribution')
plt.show()