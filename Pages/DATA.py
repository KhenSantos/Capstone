import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns

sns.set()

data= pd.read_csv("CAPSTONEDATA.csv")
df = pd.DataFrame(data)
selected_column = df[['PROJECT','COUNTRY','PROFITAFTERTAX']]
st.table(selected_column)