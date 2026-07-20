# 📊 DataLab

A modular Python-based Data Analysis Toolkit for loading, cleaning, analyzing, visualizing, and exporting CSV datasets through an interactive Command Line Interface (CLI).

---

## 🚀 Features

### 📂 Data Loading

* Load CSV files
* Validate file paths
* Save processed datasets to a new CSV file

### 🧹 Data Cleaning

* Remove duplicate rows
* Remove rows with missing values
* Fill missing values
* Clean column names
* Drop selected columns
* Remove columns containing only missing values

### 📈 Data Analysis

* View dataset shape
* Display column names
* Display data types
* Check missing values
* Generate summary statistics
* View unique values
* Display memory usage
* Calculate total memory usage
* Generate correlation matrix
* View value counts for any column

### 📊 Data Visualization

* Histogram
* Box Plot
* Count Plot
* Scatter Plot
* Line Plot
* Bar Plot
* Correlation Heatmap

---

## 📁 Project Structure

```text
DataLab/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
├── exports/
├── assets/
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaner.py
│   ├── data_analyzer.py
│   ├── data_visualizer.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Technologies Used

* Python 3.x
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Pathlib

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Mihirjain26/DataLab
```

Navigate into the project:

```bash
cd DataLab
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python src/main.py
```

The application will ask for:

1. CSV file path
2. Operation to perform
3. Save location (optional)

---

## 📌 Main Menu

```text
========== DataLab ==========

1. Clean Dataset
2. Analyze Dataset
3. Visualize Dataset
4. Save Dataset
5. Exit
```

---

## 🎯 Learning Objectives

This project was built to practice:

* Object-Oriented Programming (OOP)
* Modular software design
* Data preprocessing
* Exploratory Data Analysis (EDA)
* Data visualization
* File handling
* Python best practices
* Command Line Interface (CLI) development

---

## 🚧 Future Improvements

* Streamlit Web Interface
* Excel (.xlsx) support
* JSON support
* Interactive dashboards
* Machine Learning integration
* Data filtering and querying
* Export visualizations
* Automated report generation

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Mihir Jain**

Aspiring AI & Machine Learning Engineer

GitHub: https://github.com/Mihirjain26
