import streamlit as st
import plotly.express as px
import pandas as pd

# Page config (should come first)
st.set_page_config(page_title="Milk Collection Dashboard", page_icon="🚚", layout="wide")

# Sidebar header
logo_col, name_col = st.columns([1, 6])

with logo_col:
    st.sidebar.image("D:\\SELP\\SaviHaat\\Savihaat Logo.png", width=60)

with name_col:
    st.sidebar.markdown("<h2 style='margin-bottom:0;color:green;'>SaviHaat (OPC) Pvt. Ltd.</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='margin-top:0;color:blue;'>Empowering smarter milk collection🚚</p>", unsafe_allow_html=True)
    st.sidebar.markdown("<h4 style='text-align:center;color:green;'>Sample Project, Lomesh Kumar</h4>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    st.markdown("<h2 style='margin-bottom:0;color:blue;'>Milk Collection Dashboard</h2>", unsafe_allow_html=True)

# 📁 Upload dataset
uploaded_file = st.sidebar.file_uploader("Upload Milk Collection CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # 🧹 Clean column names
    df.columns = df.columns.str.strip().str.upper()

    # 🗓️ Convert date column if present
    if "DATE" in df.columns:
        df["DATE"] = pd.to_datetime(df["DATE"])

    # 🔍 Optional filters
    if "SHIFT" in df.columns:
        selected_shift = st.sidebar.selectbox("Select Shift", df["SHIFT"].unique())
        df = df[df["SHIFT"] == selected_shift]


    # --- 🧮 KPIs ---
    total_amount = df["AMOUNT"].sum()
    total_volume = df["QTY."].sum()
    avg_fat = df["FAT"].mean()
    avg_snf = df["SNF"].mean()  # Changed from .max() to .mean() (optional)

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric(label="📁Total Amount", value=f"{total_amount:.0f} Rs")
    kpi2.metric(label="🥛Total Qty", value=f"{total_volume:.1f} L")
    kpi3.metric(label="📋Avg FAT", value=f"{avg_fat:.1f}")
    kpi4.metric(label="📋Avg SNF", value=f"{avg_snf:.1f}")

   # --- 📊 Top 10 Members Chart ---
# Group by MEMBER CODE and sum up the quantities
    top10 = (
        df.groupby("MEMBER CODE", as_index=False)["QTY."].sum().sort_values(by="QTY.", ascending=False).head(10)
        )

    

    fig = px.bar(
        top10,
        x="MEMBER CODE",
        y="QTY.",
        color="MEMBER CODE",
        text="QTY.",
        labels={"QTY.": "Milk Quantity (L)", "MEMBER CODE": "Farmer Code"},
        title="Top 10 Farmers by Milk Quantity",
    )
    fig.update_traces(texttemplate="%{text:.1f}", textposition="outside")
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


else:
    st.info("📊Explore milk collection trends here. To explore keep your milk collection data set csv table title formate in the sequence MEMBER CODE, FAT, SNF, QTY, RATE, AMOUNT, SHIFT ")