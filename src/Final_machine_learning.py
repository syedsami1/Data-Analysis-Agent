
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class MLAnalysis:
    def __init__(self, df):
        self.df = df

    def perform_pca(self):
        """Perform PCA on the numerical data and return the components and explained variance ratio."""
        num_cols = self.df.select_dtypes(include='number').columns
        X = self.df[num_cols].dropna()
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        pca = PCA(n_components=2)
        principal_components = pca.fit_transform(X_scaled)
        
        return principal_components, pca.explained_variance_ratio_
