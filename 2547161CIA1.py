import streamlit as st
import pandas as pd

st.set_page_config(page_title="Silver Price Calculator", layout="centered")
st.title("Silver Price Calculator")

st.subheader("Enter Silver Details")

weight = st.number_input("Weight of Silver", min_value=0.0)
unit = st.selectbox("Select Unit", ["grams", "kilograms"])
price_per_gram = st.number_input("Price per gram (INR)", min_value=0.0)
currency = st.selectbox("Display Currency", ["INR", "USD"])

if unit == "kilograms":
    weight = weight * 1000

total_cost_inr = weight * price_per_gram
USD_RATE = 83

st.subheader("Total Cost")

if currency == "USD":
    st.success(f"Total Cost: ${total_cost_inr / USD_RATE:.2f} USD")
else:
    st.success(f"Total Cost: ₹{total_cost_inr:.2f} INR")

st.subheader("Historical Silver Price Trend")

price_df = pd.read_csv("historical_silver_price.csv")

st.markdown("Historical Silver Price Dataset")
st.dataframe(price_df)

price_df.columns = price_df.columns.str.strip()

price_df["Period"] = price_df["Year"].astype(str) + "-" + price_df["Month"]

price_df = price_df.rename(columns={
    "Silver_Price_INR_per_kg": "Price_per_kg"
})

filter_option = st.radio(
    "Filter Silver Price (INR per kg)",
    ["≤ 20,000", "20,000 - 30,000", "≥ 30,000"]
)

if filter_option == "≤ 20,000":
    filtered_df = price_df[price_df["Price_per_kg"] <= 20000]
elif filter_option == "20,000 - 30,000":
    filtered_df = price_df[
        (price_df["Price_per_kg"] > 20000) &
        (price_df["Price_per_kg"] < 30000)
    ]
else:
    filtered_df = price_df[price_df["Price_per_kg"] >= 30000]

st.markdown("Silver Price Chart")

if filtered_df.empty:
    st.warning("No data in selected range. Showing complete trend.")
    st.line_chart(price_df.set_index("Period")["Price_per_kg"])
else:
    st.line_chart(filtered_df.set_index("Period")["Price_per_kg"])
    st.dataframe(filtered_df)

st.caption("Data Source: historical_silver_price.csv")

st.markdown("---")
st.markdown("Developed by Ananya S Shetty")
