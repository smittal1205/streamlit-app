import streamlit as st
import pandas as pd

st.title("Sushant Grocessors 😃😂🏋️🍷")
st.write("Stock:")
stock = pd.DataFrame(
    {
        "col1":['Apple', 'Banana', 'Pear', 'Orannge'],
        "col2":[10, 20, 40, 20]
    }
)
st.write(stock)

option = st.selectbox(
    'What would you like to buy?',
    stock.col2.to_list()
)

st.write("You selected:", option)