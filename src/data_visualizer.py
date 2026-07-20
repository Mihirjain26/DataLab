import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import is_numeric_dtype

class DataVisualizer:
    
    def histogram(self,dataframe,column):
        if not column in dataframe.columns:
            raise ValueError(f"The Column Name {column} is not present in the data")
        plt.figure(figsize=(8,5))
        sns.histplot(data=dataframe,x=column)
        plt.title(f"{column} Distribution")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def boxplot(self,dataframe,column):
        if not column in dataframe.columns:
            raise ValueError(f"The Column Name {column} is not present in the data")
        if not is_numeric_dtype(dataframe[column]):
            raise ValueError(f"The Column {column} Is Not Numerical")
        plt.figure(figsize=(8,5))
        sns.boxplot(data=dataframe,y=column)
        plt.title(f"Box Plot of {column}")
        plt.ylabel(column)
        plt.xlabel("")
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def countplot(self,dataframe,column):
        if not column in dataframe.columns:
            raise ValueError(f"The Column Name {column} is not present in the data")
        if is_numeric_dtype(dataframe[column]):
            raise ValueError(f"The Column {column} is Not Categorical Hence Cannot be used for CountPlot") 
        plt.figure(figsize=(8, 5))
        sns.countplot(data=dataframe,x=column)
        plt.title(f"Count Plot of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def scatterplot(self,dataframe,column1,column2):
        if not column1 in dataframe.columns:
            raise ValueError(f"The Column Name {column1} is not present in the data")
        if not column2 in dataframe.columns:    
            raise ValueError(f"The Column Name {column2} is not present in the data")
        if not is_numeric_dtype(dataframe[column1]):
            raise ValueError(f"The Column Name {column1} is not Numerical")
        if not is_numeric_dtype(dataframe[column2]):
            raise ValueError(f"The Column Name {column2} is not Numerical")
        plt.figure(figsize=(8,5))
        sns.scatterplot(data=dataframe,x=column1,y=column2)
        plt.title(f"Scatter Plot of {column1} vs {column2}")
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def lineplot(self,dataframe,column1,column2):
        if not column1 in dataframe.columns:
            raise ValueError(f"The Column Name {column1} is not present in the data")
        if not column2 in dataframe.columns:    
            raise ValueError(f"The Column Name {column2} is not present in the data")
        if not is_numeric_dtype(dataframe[column2]):
            raise ValueError(f"The Column Name {column2} is not Numerical")
        plt.figure(figsize=(8,5))
        sns.lineplot(data=dataframe,x=column1,y=column2)
        plt.title(f"Line Plot of {column2} over {column1}")
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def barplot(self,dataframe,column1,column2):
        if not column1 in dataframe.columns:
            raise ValueError(f"The Column Name {column1} is not present in the data")
        if not column2 in dataframe.columns:    
            raise ValueError(f"The Column Name {column2} is not present in the data")
        if not is_numeric_dtype(dataframe[column2]):
            raise ValueError(f"The Column Name {column2} is not Numerical")
        plt.figure(figsize=(8,5))
        sns.barplot(data=dataframe,x=column1,y=column2)
        plt.title(f"Bar Plot of {column1} & {column2}")
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def heatmap(self,dataframe):
        numeric_df=dataframe.select_dtypes(include="number")
        if numeric_df.empty:
            raise ValueError(f"The Dataframe Does Not Have Numerical Column")
        plt.figure(figsize=(8, 8))
        sns.heatmap(data=numeric_df.corr(),annot=True,cmap="coolwarm")
        plt.title(f"Heat Map of DataFrame")
        plt.tight_layout()
        plt.show()