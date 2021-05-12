import os
from gtts import gTTS
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



st.sidebar.markdown('<b>ABOUT:</b>', unsafe_allow_html=True)

st.sidebar.markdown("Just enter a sentence or a paragraph whose sentiment you want to analyze")
st.sidebar.markdown('<b>CREATED BY:</b>', unsafe_allow_html=True)
st.sidebar.markdown('Saurabh Khanolkar')
st.sidebar.markdown('Email : saurabh.khanolkar@gmail.com')
import textblob  
from textblob import TextBlob
tt=st.text_area("Enter text here")
if st.button('Predict'):
    edu=TextBlob(tt)
    x=edu.sentiment.polarity
    if(x<0):
        t="It is a negative comment"
        st.write("NEGATIVE")
    elif(x==0):
        t="It is a neutral comment"
        st.write("NEUTRAL")
   
    else:
        t="It is a positive comment"
        st.write("POSITIVE")
    language="en"
    output=gTTS(text=t,lang=language,slow=False)
    output.save("voice.ogg")
    audio_file = open('voice.ogg', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
