class DataAnalyzer:
    def __init__(self,dataframe):
        self.dataframe=dataframe

    def get_shape(self):
        return self.dataframe.shape
    
    def get_columns(self):
        return self.dataframe.columns
    
    def get_dtypes(self):
        return self.dataframe.dtypes
    
    def get_missing_values(self):
        return self.dataframe.isnull().sum()
        
    def get_summary_statistics(self):
        return self.dataframe.describe()
    
    def get_unique_values(self,column):
        if not column in self.dataframe.columns:
            raise ValueError(f"No Column Name Found as {column}")
        return self.dataframe[column].unique()
    
    def get_memory_usage(self):
        return self.dataframe.memory_usage(deep=True)