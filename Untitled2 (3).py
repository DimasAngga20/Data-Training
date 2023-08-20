#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import streamlit as st

df = pd.read_csv("Data Science Salary 2021 to 2023.csv")

fig = go.Figure(
    data=[go.Bar(x=df["job_title"], y=df["salary"])],
    layout=go.Layout(
        title=go.layout.Title(text="Data Science Salary")
    )
)

st.title('Hello Streamlit')
st.write('''
    Streamlit: A web application framework for Python.
''')
st.plotly_chart(fig)

