# LINEAR-REGRESSION-TASK

## 💼 Salary Prediction Using Linear Regression

This project demonstrates a **Simple Linear Regression** model that predicts an employee's salary based on their years of experience.  

It is implemented in **Python** using the **Scikit-learn** library.

## 📘 Project Overview

The goal of this project is to understand how **salary** changes with **years of experience**.  

By applying a simple linear regression model, we establish a mathematical relationship:

\[
Salary = b_0 + b_1 \times Experience
\]

Where:  
- **b₀ (Intercept)** → Base salary (even with 0 years of experience)  
- **b₁ (Slope)** → Increment in salary per additional year of experience  

## 📂 Dataset Information

**Source:** [Kaggle – Salary Dataset (Simple Linear Regression)](https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression)

| Column Name | Description |
|--------------|-------------|
| `YearsExperience` | The number of years of professional experience |
| `Salary` | The annual salary (in INR) |


## 🧠 Technologies Used

- Python 🐍  
- Pandas  
- Matplotlib  
- Scikit-learn  

## 🚀 Steps to Run the Project

## Install dependencies

pip install pandas matplotlib scikit-learn

## Run the Python script (in VS Code, Colab, or Jupyter)

python salary_prediction.py

## 📊 Visualization

The plot below shows the relationship between Years of Experience and Salary:

Blue points → Actual data points

Red line → Regression line (predicted trend)

## 💡 Insights

Salary increases linearly with years of experience.

Even with 0 years of experience, a base salary (~₹25,792) is offered.

The model shows a strong positive correlation (R² ≈ 0.95).


## 📊 Visualizations
### 1️⃣ Distribution & Skewness

Plots the histogram + KDE curve for each numeric column:

Years of Experience

Salary

Age

sns.histplot(df[column], kde=True, color='skyblue')


📈 Helps identify whether the data is left/right skewed or normal.

### 2️⃣ Bar Plot

Displays average values for 3 columns (YearsExperience, Salary, and Age).

bar_data = df[['YearsExperience', 'Salary', 'Age']].mean()
sns.barplot(x=bar_data.index, y=bar_data.values, palette='viridis')


📊 Shows the relative magnitude of features.

### 3️⃣ Heatmap (Correlation)

Checks the relationship between numeric columns.

corr = df[['YearsExperience', 'Salary', 'Age']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")


🔥 Key finding:

YearsExperience and Salary have a strong positive correlation (≈ 0.97) — ideal for linear regression.

## 🧾 Future Improvements

Include additional factors like education, job role, and location.

Try Polynomial Regression for non-linear trends.

Deploy as a web app using Streamlit or Flask.

