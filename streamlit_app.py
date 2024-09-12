import streamlit as st
import pandas as pd

st.title("Here's our first table:")
st.write(pd.DataFrame(
    {
        "col1":['Apple', 'Banana', 'Pear', 'Orannge'],
        "col2":[10, 20, 40, 20]
    }
))
st.line_chart(pd.DataFrame(
    {
        "col1":['Apple', 'Banana', 'Pear', 'Orannge'],
        "col2":[10, 20, 40, 20]
    }
))