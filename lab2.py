import streamlit as st
import pandas as pd

st.set_page_config(page_title="Shopping Behaviour Analysis", layout="wide")

st.title("Shopping Behaviour Analysis Dashboard")
st.write(
    "This dashboard helps understand customer shopping behaviour "
    "using simple filters and visual graphs."
)

df = pd.read_csv("shopping_behavior_updated.csv")

# convert purchase amount from USD to INR
df["Purchase Amount INR"] = df["Purchase Amount (USD)"] * 83
purchase_col = "Purchase Amount INR"

# sidebar filters
st.sidebar.subheader("Filter Options")

gender = st.sidebar.radio(
    "Gender",
    df["Gender"].unique()
)

category = st.sidebar.selectbox(
    "Category",
    df["Category"].unique()
)

age_range = st.sidebar.slider(
    "Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (20, 60)
)

# apply filters
filtered_df = df[
    (df["Gender"] == gender) &
    (df["Category"] == category) &
    (df["Age"].between(age_range[0], age_range[1]))
]

# key performance indicators
st.subheader("Key Performance Indicators")

k1, k2, k3 = st.columns(3)

k1.metric(
    "Total Purchase (INR)",
    round(filtered_df[purchase_col].sum(), 2)
)

k2.metric(
    "Average Purchase (INR)",
    round(filtered_df[purchase_col].mean(), 2)
)

k3.metric(
    "Total Purchases",
    len(filtered_df)
)

# show filtered data
st.subheader("Filtered Data Preview")
st.dataframe(
    filtered_df[["Age", "Gender", "Category", purchase_col]].head(10)
)

# tabs for graphs
tab1, tab2, tab3 = st.tabs(
    ["Category Graph", "Age Trend", "Age vs Purchase"]
)

# bar chart
with tab1:
    st.subheader("Purchase Count by Category")
    category_data = df["Category"].value_counts()
    st.bar_chart(category_data)

# line chart
with tab2:
    st.subheader("Average Purchase by Age")
    age_data = filtered_df.groupby("Age")[purchase_col].mean()
    st.line_chart(age_data)

# scatter chart
with tab3:
    st.subheader("Age vs Purchase Amount")
    scatter_data = filtered_df[["Age", purchase_col]].dropna().head(300)
    st.scatter_chart(scatter_data, x="Age", y=purchase_col)

with st.expander("What I implemented"):
    st.write("""
    • Built an interactive dashboard using Streamlit  
    • Added sidebar filters for gender, category, and age range  
    • Converted purchase values from USD to INR  
    • Used bar, line, and scatter charts for analysis  
    • Displayed KPIs for quick insights  
    • Added a small data preview to check filtered results  
    """)
