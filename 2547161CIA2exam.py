import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Silver Sales Dashboard", layout="wide")
st.title("Silver Sales Dashboard")

sales_df = pd.read_csv("state_wise_silver_purchased_kg.csv")

st.subheader("State-wise Silver Purchase Dataset (January)")
st.dataframe(sales_df)

st.subheader("India State-wise Silver Purchases (kg)")

if os.path.exists("india_state.geojson"):
    india_map = gpd.read_file("india_state.geojson")

    india_map["NAME_1"] = india_map["NAME_1"].str.strip()
    sales_df["State"] = sales_df["State"].str.strip()

    state_total = (
        sales_df.groupby("State", as_index=False)["Silver_Purchased_kg"]
        .sum()
    )

    map_df = india_map.merge(
        state_total,
        left_on="NAME_1",
        right_on="State",
        how="left"
    )

    fig, ax = plt.subplots(figsize=(10, 10))
    map_df.plot(
        column="Silver_Purchased_kg",
        cmap="Greys",
        legend=True,
        edgecolor="black",
        ax=ax,
        missing_kwds={"color": "lightgrey", "label": "No Data"}
    )

    ax.set_title("State-wise Silver Purchases in India")
    ax.axis("off")
    st.pyplot(fig)

else:
    st.error("india_state.geojson file not found in project folder")

st.subheader("Top 5 States with Highest Silver Purchases")

top5 = (
    sales_df.sort_values(by="Silver_Purchased_kg", ascending=False)
    .head(5)
)

st.bar_chart(top5.set_index("State")["Silver_Purchased_kg"])

st.subheader("January Silver Purchase Trend Across States")

st.line_chart(
    sales_df.set_index("State")["Silver_Purchased_kg"]
)

st.dataframe(sales_df)

st.markdown("---")
st.markdown("Developed by Ananya S Shetty")
