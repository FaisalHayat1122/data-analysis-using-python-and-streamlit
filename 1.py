import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data is Here")
#uf=st.file_uploader("Upload Excel File", type=["xlsx"])

#st.subheader("Data")

df=pd.read_excel("newfile.xlsx")

df = pd.DataFrame(df)
st.subheader("Data")
#st.dataframe("df")

st.subheader("Visuals")

fig, ax = plt.subplots()
ax.bar(df["money"],df["coffee_name"])
ax.set_ylabel("Coffee Name")
ax.set_title("Money")

st.pyplot(fig)