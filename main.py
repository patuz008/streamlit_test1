# python -m streamlit run main.py
import streamlit as st
import pandas as pd
# from plotly import express as px
import openpyxl

df = pd.read_csv('melbourne.csv')

header = st.container()
dataset = st.container()
body = st.container()
footer = st.container()

with header:
    st.title ("welcome to Patrick's Data collection")
    st.text("This is for my portfolios")
with dataset:
    st.title ("My data collections")
    st.text("Analyse dataset")
    data_tab = pd.read_csv("melbourne.csv")
    st.write(data_tab.head())

    # house_type = pd.DataFrame(data_tab['Type'].value_counts())
    # st.bar_chart(house_type)
    st.subheader('The top 15 suburbs in Melbourne')
    suburb_area = pd.DataFrame(data_tab['Suburb'].value_counts()).head(15)
    st.bar_chart(suburb_area)

with body:
    st.title ("This is a data science project")
    st.text("that seeks to show insights into.....")

    
    # st.dataframe(df)
    select_col, display_col = st.columns(2)
    price_depth = select_col.slider('what will be the price_depth ?', min_value=50000, max_value=10000000, step=10000)
    # house_estimates = select_col.selectbox('How many houses are there', options={1, 2, 3, 4, 5, 'No Limit'}, index= 0)
    house_estimates = st.selectbox('How many houses are there', df['Rooms'].unique() )
    user_input = select_col.text_input('What is the most popular region ?', 'Region Name')
    st.radio ('House Type', df['Type'].unique())
    st.date_input('Enter your favorite day in the year!!')

with footer:
    st.title ("This was created.. ")
    st.text("by Techzen Pato in 2024")


