import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Sales Dashboard")

# Load data
df = pd.read_csv("sales_data.csv")

# Sidebar filters
region = st.sidebar.selectbox("Select Region", df["Region"].unique())

# Filter data
filtered_df = df[df["Region"] == region]

# Line chart
fig = px.line(filtered_df, x="Date", y="Total Revenue", title=f"Revenue Over Time in {region}")
st.plotly_chart(fig)

# Optional: Show raw data
if st.checkbox("Show raw data"):
    st.write(filtered_df)