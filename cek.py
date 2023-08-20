import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv("https://raw.githubusercontent.com/DimasAngga20/Data-Training/main/Data%20Science%20Salary%202021%20to%202023.csv")

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