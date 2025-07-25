import streamlit as st
import os

# Streamlit page configuration
st.set_page_config(
    page_title="Employee Attrition Portfolio App",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("📁 Navigation")
st.sidebar.info("Use the menu above to navigate between pages.")


st.title("👋 Welcome to My Portfolio App")
st.markdown(
  """This portfolio app showcases my data analytics projects, focusing on employee attrition analysis and loan approval insights.
  Each project demonstrates my ability to clean, analyze, and visualize data using tools like pandas, Streamlit, and Plotly Express.
This interactive portfolio showcases my practical data analytics skills using real datasets, tools, and interactive dashboards.

---

### 🧰 Tools Used & Their Roles

- **📊 pandas**  
  Used for data cleaning, transformation, aggregation, and analysis.

- **🗄️ SQLite**  
  Lightweight relational database for storing and querying structured data.

- **🌐 Streamlit**  
  Web framework used to build interactive dashboards and data exploration tools.

- **📈 Plotly Express**  
  Library for creating interactive and insightful charts and visualizations.

---

### 📁 Projects Included

#### 1. **Employee Attrition Analysis**
- **Goal**: Understand patterns behind employee turnover and attrition.
- **Tools Used**: `pandas`, `SQLite`, `Streamlit`, `Plotly Express`
- **Features**:
  - KPI metrics (total employees, attrition rate)
  - Attrition breakdown by department, gender, and job role
  - Filterable data table
  - Interactive SQL query tool

#### 2. **Loan Approval Analysis**
- **Goal**: Explore and analyze loan applications to uncover patterns and insights related to approval decisions.
- **Tools Used**: `pandas`, `Streamlit`, `Plotly Express` (optionally `SQLite` if applicable)
- **Features**:
  - Key metrics and visual trends in loan approval
  - Customer financial behavior analysis
  - Visualizations of credit score, debt-to-income ratio, employment status, and more
  - (Optional) Model-based prediction of loan approvals (if added later)

---

### 🔄 Process & Workflow

1. **Data Ingestion**: Load structured CSV or SQLite data into pandas DataFrames.
2. **Data Cleaning**: Handle missing values, fix data types, and prepare for analysis.
3. **Exploration & Analysis**: Use pandas and SQL to derive insights and trends.
4. **Visualization**: Build dashboards with Plotly and Streamlit to make findings actionable.
5. **Interactivity**: Empower users to filter, search, and query data through intuitive interfaces.

---

### 🚀 How to Use This Portfolio

Use the sidebar to navigate between projects and explore their dashboards or query tools.  
Each section demonstrates a different part of the data analysis workflow.

---

**This portfolio is built to show, not just tell — it reflects how I apply real tools to solve real-world business problems.**
"""
)
