import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns

sns.set()

st.subheader("Sales Line Chart")
data= pd.read_csv("CAPSTONEDATA.csv")

st.line_chart(data,x="PROJDATE",y="NETSALES")

st.divider()