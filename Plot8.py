df['Target'] = df['Target'].apply(lambda x: 1 if x == 'Graduate' else 0)

X = df.select_dtypes(include='number').drop(columns=['Target'])
y = df['Target']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)



#  unsupervised learning: K-Means Clustering
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_train_pca)
clusters = kmeans.predict(X_train_pca)

# Plotting 
plt.figure(figsize=(10, 6))
plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=clusters, cmap='viridis', marker='o', edgecolor='black', s=50, alpha=0.6)
plt.title('K-Means Clustering')
plt.xlabel('Martial Status')
plt.show()

(rf_accuracy, rf_report)