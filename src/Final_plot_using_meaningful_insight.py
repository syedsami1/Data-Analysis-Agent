# src/Final_plot_using_meaningful_insight.py
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

class PlotAgent:
    def __init__(self, df):
        self.df = df

    def plot_histograms(self, num_cols):
        """Create histograms for numerical columns."""
        plots = []
        for num_col in num_cols:
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(self.df[num_col], kde=True)
            plt.title(f'Distribution of {num_col}')
            plots.append(fig)
        return plots

    def plot_countplots(self, cat_cols):
        """Create count plots for categorical columns."""
        plots = []
        for cat_col in cat_cols:
            fig = plt.figure(figsize=(10, 6))
            sns.countplot(y=self.df[cat_col])
            plt.title(f'Distribution of {cat_col}')
            plots.append(fig)
        return plots

    def plot_interactive(self, num_cols):
        """Create interactive plots for numerical columns."""
        for num_col in num_cols:
            fig = px.histogram(self.df, x=num_col, title=f'Interactive Distribution of {num_col}')
            fig.show()
