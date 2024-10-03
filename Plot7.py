categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()



preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])


X_cluster = preprocessor.fit_transform(df)

# Elbow method
sse = {}
for k in range(1, 5):  
    kmeans = KMeans(n_clusters=k, random_state=42).fit(X_cluster)
    sse[k] = kmeans.inertia_  


plt.figure(figsize=(10, 6))
plt.plot(list(sse.keys()), list(sse.values()), marker='o')
plt.title('Elbow Method for Determining k')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Sum of squared distances')
plt.xticks(list(sse.keys()))
plt.show()