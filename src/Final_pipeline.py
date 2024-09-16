# src/Final_pipeline.py
import pandas as pd

class SaleDataPipeline:
    def __init__(self, file):
        self.file = file
        self.df = None
    
    def load_data(self):
        # Determine the file extension and specify the engine accordingly
        if self.file.name.endswith('.csv'):
            self.df = pd.read_csv(self.file)
        elif self.file.name.endswith('.xlsx'):
            self.df = pd.read_excel(self.file, engine='openpyxl')  # Specify the engine
        else:
            raise ValueError("Unsupported file format. Please upload a .csv or .xlsx file.")
        return self.df

    def describe_data(self):
        return self.df.describe(include='all')
    
    def get_columns(self):
        num_cols = self.df.select_dtypes(include='number').columns.tolist()
        cat_cols = self.df.select_dtypes(include='object').columns.tolist()
        return num_cols, cat_cols
