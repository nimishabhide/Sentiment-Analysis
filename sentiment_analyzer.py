python -m pip install textblob
import streamlit as st
html_temp = """
    <div style="background-color:black ;padding:10px">
    <h1 style="color:white;text-align:center;">Sentiment Analyzer</h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

html_temp69 = """
    <div style="background-color:white ;padding:10px">
    </div>
    """
st.markdown(html_temp69, unsafe_allow_html=True)






st.sidebar.header("ANALYSE DATA AT THE CLICK OF A BUTTON!")

st.sidebar.markdown('<b>ABOUT:</b>', unsafe_allow_html=True)

st.sidebar.markdown("Just enter a sentence or a paragraph whose sentiment you want to identify")
st.sidebar.markdown('<b>CREATED BY:</b>', unsafe_allow_html=True)
st.sidebar.markdown('Nimisha Bhide')
st.sidebar.markdown('Email : nbhide.nb@gmail.com')
  
from textblob import TextBlob
tt=st.text_area("Enter text here")
edu=TextBlob(tt)
x=edu.sentiment.polarity
if(x<0):
  st.write("NEGATIVE")
elif(x==0):
  st.write("NEUTRAL")
else:
  st.write("POSITIVE")

