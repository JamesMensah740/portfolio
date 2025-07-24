import streamlit as st
import pandas as pd
import plotly.express as px

# Config
st.set_page_config(page_title="Loan Risk Analysis", layout="wide")
st.title("💰 Loan Approval & Risk Analysis")
st.markdown("""
Analyze a real-world loan dataset to identify patterns in approvals and financial risk levels.
This interactive dashboard highlights key drivers of lending decisions using **pandas** and **Plotly**.
""")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/loan_data.csv")
    df['RiskBucket'] = pd.cut(df['RiskScore'], bins=[0, 40, 70, 100], labels=["High Risk", "Medium Risk", "Low Risk"])
    return df

df = load_data()

# === Section 1: Dataset Explorer ===
st.header("🔍 Dataset Explorer")
with st.expander("View full dataset"):
    st.dataframe(df)

# Filter for analysis
st.sidebar.header("📌 Filters")
selected_education = st.sidebar.multiselect("Education Level", df['EducationLevel'].unique(), default=df['EducationLevel'].unique())
selected_status = st.sidebar.multiselect("Employment Status", df['EmploymentStatus'].unique(), default=df['EmploymentStatus'].unique())
selected_risk = st.sidebar.multiselect("Risk Bucket", df['RiskBucket'].unique(), default=df['RiskBucket'].unique())

filtered_df = df[
    (df['EducationLevel'].isin(selected_education)) &
    (df['EmploymentStatus'].isin(selected_status)) &
    (df['RiskBucket'].isin(selected_risk))
]

# === Section 2: Loan Approval Insights ===
st.header("✅ Loan Approval Insights")

approval_fig = px.histogram(filtered_df, x="LoanApproved", color="LoanApproved",
                            title="Loan Approval Count", text_auto=True)
st.plotly_chart(approval_fig, use_container_width=True)

approval_by_employment = pd.crosstab(filtered_df['EmploymentStatus'], filtered_df['LoanApproved'], normalize='index')
approval_by_employment_fig = px.bar(approval_by_employment, barmode="group",
                                    title="Approval Rate by Employment Status")
st.plotly_chart(approval_by_employment_fig, use_container_width=True)

# === Section 3: Risk Score Analysis ===
st.header("📉 Risk Score & Buckets")

risk_dist = px.histogram(filtered_df, x="RiskScore", nbins=30, color="RiskBucket",
                         title="Risk Score Distribution by Risk Bucket")
st.plotly_chart(risk_dist, use_container_width=True)

risk_bucket_count = filtered_df['RiskBucket'].value_counts().reset_index()
risk_bucket_count.columns = ["RiskBucket", "Count"]
risk_bucket_fig = px.bar(risk_bucket_count, x="RiskBucket", y="Count",
                         color="RiskBucket", title="Applicants per Risk Tier")
st.plotly_chart(risk_bucket_fig, use_container_width=True)

# === Section 4: Feature Exploration ===
st.header("📊 Feature Exploration")

x_feature = st.selectbox("X-axis Feature", ['CreditScore', 'AnnualIncome', 'LoanAmount', 'DebtToIncomeRatio'])
y_feature = st.selectbox("Y-axis Feature", ['InterestRate', 'RiskScore', 'MonthlyLoanPayment'])

scatter = px.scatter(filtered_df, x=x_feature, y=y_feature, color='LoanApproved',
                     size='LoanAmount', hover_data=['Age', 'EducationLevel'],
                     title=f"{y_feature} vs {x_feature}")
st.plotly_chart(scatter, use_container_width=True)

# === Section 5: High Risk Applicants Table ===
st.header("🚨 High Risk Applicants")
st.dataframe(filtered_df[filtered_df['RiskBucket'] == "High Risk"][[
    'Age', 'CreditScore', 'AnnualIncome', 'LoanAmount',
    'RiskScore', 'LoanApproved', 'EmploymentStatus'
]])

# === Section 6: Summary ===
st.header("📌 Key Takeaways")
st.markdown("""
- **Loan approval** is influenced by multiple factors, including **credit score**, **employment status**, and **debt ratio**.
- Applicants in the **High Risk** tier generally have lower credit scores and higher debt-to-income ratios.
- **Education and employment** play a role in approval likelihood.
- Use this tool to explore how applicant profiles relate to approval and risk.

---
Built with pandas + Plotly + Streamlit | By **James Mensah**
""")
