from data_loader import DataLoader
from data_cleaner import DataCleaner
from data_analyzer import DataAnalyzer
from data_visualizer import DataVisualizer


def cleaning_menu(dataframe,cleaner):
    while True:
        print("======Cleaning Menu======")
        print("\n1. Remove Duplicates")
        print("2. Remove Missing Values")
        print("3. Fill Missing Values")
        print("4. Clean Column Names")
        print("5. Drop Columns")
        print("6. Drop Null Columns")
        print("7. Back")
        choice=input("Enter Your Choice")
        if choice=="1":
            dataframe = cleaner.remove_duplicates(dataframe)
            print("Duplicates removed successfully.\n")
        
        elif choice=="2":
            dataframe=cleaner.remove_missing_values(dataframe)
            print("Missing Values removed successfully.\n")

        elif choice=="3":
            fill_value = input("Enter the value to fill missing values with: ")
            dataframe=cleaner.fill_missing_values(dataframe,fill_value)
            print("Data Filled successfully.\n")

        elif choice=="4":
            dataframe = cleaner.clean_column_names(dataframe)
            print("Column names cleaned successfully.\n")
        
        elif choice=="5":
            column_name=input("Enter the column to drop: ")
            dataframe=cleaner.drop_columns(dataframe,column_name)
            print("Column dropped successfully.\n")
        
        elif choice=="6":
            dataframe=cleaner.drop_null_columns(dataframe)
            print("Columns containing only missing values removed successfully.\n")

        elif choice=="7":
            print("Back to Main Menu\n")
            return dataframe
        
        else:
            print("Invalid Choice")
        







def analyzer_menu(dataframe,analyzer):
    while True:
        print("""====== Analyzer Menu ======

    1. Dataset Shape
    2. Column Names
    3. Data Types
    4. Missing Values
    5. Summary Statistics
    6. Unique Values
    7. Memory Usage
    8. Total Memory Usage
    9. Correlation Matrix
    10. Value Counts
    11. Back""")
        choice=input("Enter Your Choice: ")
        if choice=="1":
            print(analyzer.get_shape(dataframe))
        
        elif choice=="2":
            print(analyzer.get_columns(dataframe))
        
        elif choice=="3":
            print(analyzer.get_dtypes(dataframe))
        
        elif choice=="4":
            print(analyzer.get_missing_values(dataframe))
        
        elif choice=="5":
            print(analyzer.get_summary_statistics(dataframe))
        
        elif choice=="6":
            column_name=input("Enter the Column Name: ")
            print(analyzer.get_unique_values(dataframe,column_name))
        
        elif choice=="7":
            print(analyzer.get_memory_usage(dataframe))
        
        elif choice=="8":
            print(analyzer.get_total_memory_usage(dataframe))
        
        elif choice=="9":
            print(analyzer.get_correlation_matrix(dataframe))
        
        elif choice=="10":
            column_name=input("Enter the Column Name: ")
            print(analyzer.get_value_counts(dataframe,column_name))
        
        elif choice=="11":
            return dataframe
        
        else:
            print("Invalid Choice")




def visualizer_menu(dataframe,visualizer):
    while True:
        print("""\n====== Visualization Menu ======

    1. Histogram
    2. Box Plot
    3. Count Plot
    4. Scatter Plot
    5. Line Plot
    6. Bar Plot
    7. Heatmap
    8. back
    """)
        choice=input("Enter Your Choice")

        if choice=="1":
            column_name=input("Enter Column Name: ")
            visualizer.histogram(dataframe,column_name)

        elif choice=="2":
            column_name=input("Enter Column Name: ")
            visualizer.boxplot(dataframe,column_name)

        elif choice=="3":
            column_name=input("Enter Column Name: ")
            visualizer.countplot(dataframe,column_name)

        elif choice=="4":
            x_column=input("Enter X-axis column: ")
            y_column=input("Enter Y-axis column: ")
            visualizer.scatterplot(dataframe,x_column,y_column)

        elif choice=="5":
            x_column=input("Enter X-axis column: ")
            y_column=input("Enter Y-axis column: ")
            visualizer.lineplot(dataframe,x_column,y_column)

        elif choice=="6":
            x_column=input("Enter X-axis column: ")
            y_column=input("Enter Y-axis column: ")
            visualizer.barplot(dataframe,x_column,y_column)

        elif choice=="7":
            visualizer.heatmap(dataframe)

        elif choice=="8":
            print("Back to Main Menu")
            return dataframe
        else:
            print("Invalid Choice")
            




def main():

    loader = DataLoader()
    cleaner = DataCleaner()
    analyzer = DataAnalyzer()
    visualizer = DataVisualizer()

    file_path=input("Enter the CSV file path: ")
    dataframe = loader.load_csv(file_path)
    print("\nDataset loaded successfully!")

    while True:
        print("\n==========DataLab==========")
        print("1. Clean Dataset")
        print("2. Analyze Dataset")
        print("3. Visualize Dataset")
        print("4. Save Dataset")
        print("5. Exit")
        choice=input("Enter your choice")

        if choice=="1":
            dataframe=cleaning_menu(dataframe,cleaner)

        elif choice=="2": 
            dataframe=analyzer_menu(dataframe,analyzer)

        elif choice=="3": 
            dataframe=visualizer_menu(dataframe,visualizer)

        elif choice=="4": 
            output_path=input("Enter the Path where you want to save the CSV file")
            loader.save_csv(dataframe,output_path)
            print("Dataset Saved Successfully.")

        elif choice=="5":
            print("Thank you for using DataLab!")
            break

        else:
            print("Invalid Choice")

