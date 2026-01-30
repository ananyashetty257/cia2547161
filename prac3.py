import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime,time
import matplotlib.pyplot as plt

st.title("Streamlit Widgets Demonstration App")
st.header(" an overview as streamlit features")
st.subheader("Streamlit is an amazing tool for interactive web applications.")

st.text("This is a simple text output using the text element")
st.write("you can also write to render Markdown,Dataframes,or other objects")

st.markdown("### Markdown Example")
st.markdown("Streamlit supports **Markdown**,including: \n- *Italic* \n- **Bold** \n- `Code Blocks`")

st.code("st.title('Streamlit App')", language="python")

st.markdown("### Metrics widgets")
st.metric(label = "Revenue",value="$120,000",delta ="$5,000",delta_color="inverse")
st.metric(label = "User Growth",value="$120,000",delta ="-200",delta_color="normal")

st.subheader(" Selectbox Widget")

agree = st.checkbox("I agree")

feedback = st.feedback("thumbs")

tags = st.pills("Tags",["Sports","Politics","Education"])

choice_radio = st.radio("pick one",["Cat","Dog"])

status = st.segmented_control("Filter",["Open","Closed"])

enable = st.toggle("Enable feature")

choice_select = st.selectbox("pick one",["Cat","Dog"])

shopping = st.multiselect("Buy",["milk","bread","eggs"])

st.subheader("Slider and inputs")

number = st.slider("Select a number", 0, 100)

size =st.select_slider("Select size",["Small","Medium","Large"])

name = st.text_input("Enter your name")

num_input = st.number_input("Pick a number", 0,10)

text = st.text_area("Text to translate")

st.subheader("Date and Time Widgets")

birthday = st.date_input("Select your birthday",)

meeting_time = st.time_input("Select meeting time",time(9, 0))

st.subheader("File and media Inputs")

uploaded_file = st.file_uploader("Upload a csv")
if uploaded_file:
    df_uploaded = pd.read_csv(uploaded_file)
    st.dataframe(df_uploaded)

audio = st.audio_input("Record audio")

photo = st.camera_input("Take a photo")

color = st.color_picker("Pick a color")

st.subheader("User Input Summary")

st.write({
    "Agreed ":agree,
    "Feedback":feedback,
    "Tags":tags,
    "Radio Choice":choice_radio,
    "Status":status,
    "Enabled":enable,
    "Selectbox Choice":choice_select,
    "Shopping List":shopping,
    "Number":number,
    "Size":size,
    "Name":name,
    "Number Input":num_input,
    "Text":text,
    "Birthday":birthday,
    "Meeting Time":meeting_time,
    "Uploaded File":uploaded_file is not None,
    "Audio Recorded":audio is not None,
    "Photo Taken":photo is not None,
    "Color":color
})

st.set_page_config(
    page_title="Streamlit Widgets Demo",
    page_icon=":shark:",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Streamlit Widgets Demonstration App")

data = pd.DataFrame({
    "Month": ["January", "February", "March", "April"],
    "Sales": [1000, 1500, 2000, 2500],
    "Profit": [200, 300, 400, 500]
})

st.subheader("Sales Data")

st.write(data)
st.write("This table shows the sales and profit data for each month.")

st.write("Sales Over Months")
st.table(data)

st.write("Profit Over Months")
st.dataframe(data)

st.subheader("Sales and Profit Bar Chart")

st.line_chart(data.set_index("Month")[["Sales","Profit"]])
st.bar_chart(data.set_index("Month")[["Sales","Profit"]])
st.area_chart(data.set_index("Month")[["Sales","Profit"]])

st.subheader("Sales and Profit Pie Chart")
fig, ax = plt.subplots()
ax.plot(data["Month"],data["Sales"],marker="o",label="Sales")
ax.plot(data["Month"],data["Profit"],marker="o",label="Profit")
ax.set_xlabel("Month")
ax.set_ylabel("Amount")
ax.set_title("Sales and Profit Over Months")
ax.legend()

st.pyplot(fig)
st.subheader("Sales and Profit Scatter Plot")

with st.form("my_form"):
    st.write("Please fill out the form below:")
    name = st.text_input("Name")
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Submit")
    
if submit_button:
    st.success(f"Thank you {name} for submitting the form!")
