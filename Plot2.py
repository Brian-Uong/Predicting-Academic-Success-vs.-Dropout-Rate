# Ensure 'Marital status' column is treated as a category
df['Marital status'] = pd.Categorical(df['Marital status'])

# Calculate the percentages and filter out any category that makes up less than 1% of the total
marital_status_percentages = df['Marital status'].value_counts(normalize=True, dropna=True) * 100
marital_status_filtered = marital_status_percentages[marital_status_percentages > 1]

# Prepare the labels for the pie chart, corresponding to the filtered categories
labels_filtered = {1: 'Single', 2: 'Married', 3: 'Other'}  # Assuming these are the only relevant categories
labels_to_use = [labels_filtered.get(key, 'Other') for key in marital_status_filtered.index]

# Generate the pie chart with the filtered values and labels
plt.figure(figsize=(8, 6))
plt.pie(marital_status_filtered, labels=labels_to_use, autopct=lambda p: '{:.1f}%'.format(p) if p > 1 else '', startangle=140, colors=["#ADD8E6", "pink", "lightgreen"])
plt.title('Marital Status Distribution ')
plt.show()