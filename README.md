# Personal Finance Analyzer

**A hands-on Python project to learn Pandas, Streamlit, and data analysis by building a personal finance dashboard.**

## Why I Built This Project

I built this project to understand how data analysis works in practice and learn how to use Python libraries such as Pandas and Streamlit.

Rather than learning each library only through isolated examples, I wanted to apply them to a practical problem: analyzing bank transaction data and presenting the results in an interactive dashboard.

This project gave me an opportunity to work with CSV files, clean and process data, perform calculations, create visualizations, and connect the analysis to a user interface.

My primary goal was to learn by building. The finance analyzer is a starting point that I can improve as I gain a better understanding of data processing, application development, and eventually machine learning.

## What I Have Implemented

### 1. Data Processing with Pandas
- Read transaction data from CSV files.
- Clean column names by removing unnecessary whitespace.
- Convert transaction dates into a datetime format.
- Filter transactions based on dates and categories.
- Calculate income, expenses, net savings, and category-wise spending.

### 2. Transaction Categorization
I implemented a basic rule-based function that categorizes transactions by checking keywords in their descriptions.

For example, descriptions containing keywords such as `Swiggy`, `Uber`, or `Netflix` can be assigned to categories such as Food, Transport, or Entertainment.

This helped me understand how to process text data and apply custom Python functions to a Pandas DataFrame.

The current implementation uses predefined rules rather than a trained machine-learning model.

### 3. Interactive Dashboard with Streamlit
I used Streamlit to turn the data-processing logic into an interactive application.

The dashboard includes:
- CSV file upload
- Date and category filters
- Income, expenses, and savings summaries
- Bar and pie charts for spending analysis
- A table displaying the filtered transactions
- Basic insights generated from the transaction data

### 4. Modular Python Code
I separated different responsibilities into multiple Python files to understand how a project can be organized into smaller, manageable components.

- `app.py` — Dashboard and user interaction
- `data_preprocessing.py` — CSV loading and data preparation
- `categorization.py` — Rule-based transaction categorization
- `analytics.py` — Financial calculations
- `insights.py` — Basic financial insights
- `main.py` — An earlier standalone version of parts of the analysis

## What I Learned

Through this project, I worked on:

- Using Pandas to read, clean, filter, and analyze tabular data.
- Working with dates and numerical transaction values.
- Applying custom functions to transaction descriptions.
- Calculating summary statistics and grouping data by category.
- Creating charts to communicate the results of data analysis.
- Building an interactive interface using Streamlit.
- Separating data processing, analysis, and presentation into different modules.
- Debugging issues that arise when connecting multiple components.

## What I Want to Implement Next

The current project is a learning prototype. My next objective is to strengthen the existing implementation before adding more advanced features.

### 1. Improve Data Handling
I want to make the application more reliable when it receives transaction data with inconsistent date formats, missing values, or unexpected descriptions.

**My approach:** Improve the preprocessing functions, add validation checks, and test the application with different CSV datasets.

### 2. Improve Transaction Categorization
The current keyword-based approach is simple, but it cannot reliably classify every transaction.

**My approach:** First improve the existing rules and explore ways for users to correct categories. After understanding the limitations of this baseline, I want to investigate whether machine learning could improve categorization accuracy.

### 3. Add Monthly Spending Analysis
I want to understand how spending patterns change over time instead of showing only an overall summary.

**My approach:** Use Pandas date-based grouping to calculate monthly income, expenses, and category-wise spending, then display the results using Streamlit charts.

### 4. Explore Budget Tracking and Better Insights
I eventually want users to compare actual spending with their budgets and identify meaningful changes in their spending patterns.

**My approach:** Build category-wise budget comparisons first, followed by simple, explainable insights based on historical transactions. I will explore forecasting only after the underlying data and calculations are reliable.

These features are planned improvements, not part of the current implementation.

## Technology Stack

- Python
- Pandas
- Streamlit
- Matplotlib

## Running the Project

Clone the repository:

```bash
git clone https://github.com/Sarthak180403/Finance_analyser.git
cd Finance_analyser
```

Create and activate a virtual environment on Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required libraries:

```bash
pip install streamlit pandas matplotlib
```

Run the application:

```bash
streamlit run app.py
```

Upload a CSV containing the transaction fields expected by the current implementation to explore the dashboard.

## Project Status

This project began as a way for me to learn Pandas and Streamlit through hands-on development. I have implemented the basic data-processing workflow, rule-based categorization, financial summaries, and interactive visualizations.

I intend to continue developing it by improving data reliability, exploring more effective categorization methods, and adding useful financial analysis features as I learn more.

**The main objective is to keep learning by building, testing, and improving a working application.**
