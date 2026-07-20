class DataAnalyzer:

    def get_shape(self,dataframe):
        return dataframe.shape
    
    def get_columns(self,dataframe):
        return dataframe.columns
    
    def get_dtypes(self,dataframe):
        return dataframe.dtypes
    
    def get_missing_values(self,dataframe):
        return dataframe.isnull().sum()
        
    def get_summary_statistics(self,dataframe):
        return dataframe.describe(include="all")
    
    def get_unique_values(self,dataframe,column):
        if not column in dataframe.columns:
            raise ValueError(f"No Column Name Found as {column}")
        return dataframe[column].unique()
    
    def get_memory_usage(self,dataframe):
        return dataframe.memory_usage(deep=True)
    
    def get_total_memory_usage(self,dataframe):
        return dataframe.memory_usage(deep=True).sum()
    
    def get_correlation_matrix(self,dataframe):
        return dataframe.select_dtypes(include=['number']).corr()
    
    def get_value_counts(self,dataframe,column):
        if not column in dataframe.columns:
            raise ValueError(f"No Column Name Found as {column}")
        return dataframe[column].value_counts()