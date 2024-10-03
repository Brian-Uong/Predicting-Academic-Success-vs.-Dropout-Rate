gender = df['Gender']
course = df['Course']

gender_course_count = df.groupby(['Gender', 'Course']).size().unstack()

plt.figure(figsize=(12, 6))
gender_course_count.plot(kind='bar', stacked=True, alpha=0.8)
plt.title('Frequency of Gender by Course')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.legend(title='Course', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()