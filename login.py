import streamlit as st
import pandas as pd
from datetime import time
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Streamlit Widgets Demo",
    layout="centered"
)

if "login" not in st.session_state:
    st.session_state.login = False

st.sidebar.title("Login")

EMAIL = "user@gmail.com"
PASSWORD = "streamlit"

if not st.session_state.login:
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if email == EMAIL and password == PASSWORD:
            st.session_state.login = True
            st.rerun()
        else:
            st.sidebar.error("Invalid credentials")
    st.stop()

if st.sidebar.button("Logout"):
    st.session_state.login = False
    st.rerun()

st.title("Streamlit Widgets Demonstration App")
st.header("An overview of Streamlit features")
st.subheader("Streamlit is an amazing tool for interactive web applications")

st.text("This is a simple text output")
st.write("st.write can render text, markdown, tables, and more")

st.markdown("### Markdown Example")
st.markdown(
    "- *Italic*\n- **Bold**\n- `Code`"
)

st.markdown("### Metrics")
st.metric("Revenue", "$120,000", "+$5,000")
st.metric("Users", "2,500", "+200")

agree = st.checkbox("I agree")
name = st.text_input("Enter your name")
number = st.slider("Select a number", 0, 100)
birthday = st.date_input("Birthday")
meeting = st.time_input("Meeting Time", time(9, 0))

file = st.file_uploader("Upload CSV file")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [1000, 1500, 2000, 2500]
})

st.subheader("Sales Chart")
st.line_chart(data.set_index("Month"))

fig, ax = plt.subplots()
ax.bar(data["Month"], data["Sales"])
st.pyplot(fig)

st.success("Logged in")
