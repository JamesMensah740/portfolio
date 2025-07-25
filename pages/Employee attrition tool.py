import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
from utils.db import run_query

st.set_page_config(page_title="📊 Employee attrition tool", layout="wide")

# === SIDEBAR SECTION SELECTOR ===
st.sidebar.title("Navigation")
section = st.sidebar.radio("Choose a section:", ["Dashboard", "SQL Query Tool"])

# === Load Data with Caching ===
@st.cache_data
def load_data():
    query = "SELECT * FROM employee_attrition"
    return pd.DataFrame(run_query(query))

df = load_data()

# === DASHBOARD SECTION ===
if section == "Dashboard":
    st.title("📊 Employee Attrition Dashboard")

    # --- KPI Section ---
    total_employees = len(df)
    total_attrition = df[df['Attrition'] == 'Yes'].shape[0]
    attrition_rate = round((total_attrition / total_employees) * 100, 2)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Employees", total_employees)
    col2.metric("Attrition Count", total_attrition)
    col3.metric("Attrition Rate (%)", attrition_rate)

    # --- Attrition by Department ---
    st.subheader("Attrition by Department")
    dept_counts = df.groupby('Department')['Attrition'].value_counts().unstack().fillna(0)
    dept_counts['Attrition Rate (%)'] = (dept_counts['Yes'] / dept_counts.sum(axis=1)) * 100

    fig1 = px.bar(
        dept_counts,
        y=dept_counts.index,
        x='Attrition Rate (%)',
        orientation='h',
        title="Attrition Rate by Department",
        color='Attrition Rate (%)',
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # --- Attrition by Gender and Job Role ---
    st.subheader("Attrition by Gender and Job Role")
    fig2 = px.sunburst(
        df[df['Attrition'] == 'Yes'],
        path=['Gender', 'JobRole'],
        values=None,
        title="Attrited Employees by Gender and Role"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # --- Optional: Filter and explore ---
    st.subheader("Filterable Table View")
    with st.expander("🔍 Filter Data"):
        selected_department = st.multiselect("Filter by Department", df['Department'].unique())
        selected_gender = st.multiselect("Filter by Gender", df['Gender'].unique())
        selected_job_role = st.multiselect("Filter by Job Role", df['JobRole'].unique())
        selected_attrition = st.multiselect("Filter by Attrition", df['Attrition'].unique())

        filtered_df = df.copy()
        if selected_department:
            filtered_df = filtered_df[filtered_df['Department'].isin(selected_department)]
        if selected_gender:
            filtered_df = filtered_df[filtered_df['Gender'].isin(selected_gender)]
        if selected_job_role:
            filtered_df = filtered_df[filtered_df['JobRole'].isin(selected_job_role)]
        if selected_attrition:
            filtered_df = filtered_df[filtered_df['Attrition'].isin(selected_attrition)]

        st.dataframe(filtered_df)

# === SQL QUERY TOOL SECTION ===
elif section == "SQL Query Tool":
    st.title("SQL Query Tool")
    st.markdown("Write SQL queries to explore the employee database.")

    default_query = "SELECT * FROM employee_attrition LIMIT 10"
    query = st.text_area("SQL Query", default_query, height=150)

    if st.button("Run Query"):
        try:
            result = pd.DataFrame(run_query(query))
            st.dataframe(result)
        except Exception as e:
            st.error(f"Error: {e}")

st.header("📌 Key Takeaways")
st.markdown("""
- **Loan approval** is influenced by multiple factors, including **credit score**, **employment status**, and **debt ratio**.
- Applicants in the **High Risk** tier generally have lower credit scores and higher debt-to-income ratios.
- **Education and employment** play a role in approval likelihood.
- Use this tool to explore how applicant profiles relate to approval and risk.

---
Built with SQLite3 + Pandas + Plotly + Streamlit | By **James Mensah**
""")