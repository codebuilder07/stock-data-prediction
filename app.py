import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import pandas_datareader as data not working,not used in code
import yfinance as yf   #this is used instead
from keras.models import load_model
import streamlit as st
import datetime


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2022, 12, 31)

st.title('Stock Trend Prediction')
user_input=st.text_input('Enter the Stock Ticker','AAPL')
df= yf.download(user_input, start=start, end=end)

#describing data
st.subheader('Date from 2010 to 2022')
st.write(df.describe())

#VISUALIZATION
st.subheader('Closing Price vs Time')
fig= plt.figure(figsize =(12,6))
plt.plot(df.Close)
st.pyplot(fig)


st.subheader('Closing Price vs Time with 100ma')
ma100=df.Close.rolling(100).mean()
fig= plt.figure(figsize =(12,6))
plt.plot(ma100,"r")
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time with 100ma & 200ma')
ma100=df.Close.rolling(100).mean()
ma200=df.Close.rolling(200).mean()
fig= plt.figure(figsize =(12,6))
plt.plot(ma100,"r")
plt.plot(ma200,"g")
plt.plot(df.Close)
st.pyplot(fig)