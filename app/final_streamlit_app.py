# app/final_streamlit_app.py
import streamlit as st
import pandas as pd
import sys
import os

# Add the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from Final_pipeline import SaleDataPipeline
from Final_plot_using_meaningful_insight import PlotAgent
from Final_machine_learning import MLAnalysis

def main():
    st.title("Data Analysis Agent")

    # User uploads file
    uploaded_file = st.file_uploader("Upload your file", type=['xlsx', 'csv'])

    if uploaded_file:
        # Initialize data pipeline with the uploaded file
        data_pipeline = SaleDataPipeline(uploaded_file)
        df = data_pipeline.load_data()

        # Display data
        st.write("### Data Preview")
        st.write(df.head())

        # Display descriptive statistics
        st.write("### Descriptive Statistics")
        st.write(data_pipeline.describe_data())

        # Get columns
        num_cols, cat_cols = data_pipeline.get_columns()

        # Create and display plots
        plot_agent = PlotAgent(df)
        
        st.write("### Numerical Data Distributions")
        num_plots = plot_agent.plot_histograms(num_cols)
        for plot in num_plots:
            st.pyplot(plot)

        st.write("### Categorical Data Distributions")
        cat_plots = plot_agent.plot_countplots(cat_cols)
        for plot in cat_plots:
            st.pyplot(plot)
        
        st.write("### Interactive Plots")
        plot_agent.plot_interactive(num_cols)

        # Perform PCA and show results
        st.write("### PCA Analysis")
        ml_analysis = MLAnalysis(df)
        components, variance_ratio = ml_analysis.perform_pca()
        st.write(f"PCA Components:\n{components}")
        st.write(f"Explained Variance Ratio:\n{variance_ratio}")

if __name__ == "__main__":
    main()
