import streamlit as st
import pandas as pd
from utils.db import run_query

st.set_page_config(page_title="SQL Playground", layout="wide")
st.title("🧪 SQL Query Playground")

default_query = """
SELECT department, COUNT(*) AS headcount,
       SUM(attrition = 'Yes') AS attrited
FROM employee_attrition
GROUP BY department;
"""

query = st.text_area("Write your SQL query here:", value=default_query, height=200)

if st.button("Run Query"):
    try:
        result = pd.DataFrame(run_query(query))
        st.success(f"Query executed successfully. {len(result)} rows returned.")
        st.dataframe(result)
    except Exception as e:
        st.error(f"Error: {str(e)}")
