# plot the course frequency
courses = df['Course'].value_counts()

plt.figure(figsize=(6, 7))
courses.plot(kind='pie', autopct='%1.1f%%', startangle=60)
plt.title('Course')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.tight_layout()
plt.show()