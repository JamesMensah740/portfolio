import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Loan Risk Analysis", layout="wide")
st.title("💰 Loan Approval & Risk Analysis")
st.markdown("""
This project explores a dataset of loan applications to uncover patterns in approval decisions and financial risk.
The goal is to provide insights that support better lending decisions using **pandas** and **data visualization**.
""")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data\Loan new datset.csv")  

df = load_data()

# Preview dataset
st.subheader("📄 Data Preview")
st.dataframe(df.head())

# Summary statistics
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# Loan Approval Distribution
st.subheader("✅ Loan Approval Breakdown")
approval_counts = df['LoanApproved'].value_counts()
st.bar_chart(approval_counts)

# Risk Score Distribution
st.subheader("📉 Risk Score Distribution")
fig, ax = plt.subplots()
sns.histplot(df['RiskScore'], kde=True, bins=20, ax=ax)
st.pyplot(fig)

# Approval Rate by Employment Status
st.subheader("📌 Approval Rate by Employment Status")
employment_approval = df.groupby("EmploymentStatus")['LoanApproved'].value_counts(normalize=True).unstack().fillna(0)
st.bar_chart(employment_approval)

# Credit Score vs Interest Rate
st.subheader("📈 Credit Score vs Interest Rate")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x="CreditScore", y="InterestRate", hue="LoanApproved", ax=ax2)
st.pyplot(fig2)

# Risk Buckets (Optional Insight)
st.subheader("🧠 Risk Buckets")
df['RiskBucket'] = pd.cut(df['RiskScore'], bins=[0, 40, 70, 100], labels=["High Risk", "Medium Risk", "Low Risk"])
bucket_counts = df['RiskBucket'].value_counts()
st.bar_chart(bucket_counts)

# Optional filter: Show high risk applicants
with st.expander("🔍 View High Risk Applicants"):
    st.dataframe(df[df['RiskBucket'] == "High Risk"][['Age', 'CreditScore', 'AnnualIncome', 'LoanAmount', 'RiskScore', 'LoanApproved']])

# Footer
st.markdown("---")
st.caption("Built using pandas + Streamlit | Project by James Mensah")
