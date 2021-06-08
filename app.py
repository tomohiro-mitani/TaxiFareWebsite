import streamlit as st
import requests
import os

'''
# Flashcard
'''
def load_page():
    url = 'https://n1-flashcards-api.herokuapp.com/random'
    response = requests.get(
        url
    ).json()

    st.write(response["vocab"])
    title = st.text_input('What does this mean?', 'Write your answer here.')

    if st.button('Check the answer'):
        st.write(response)
    else:
        st.write('')


def refresher():
  mainDir = os.path.dirname(__file__)
  filePath = os.path.join(mainDir, 'dummy.py')
  f = open(filePath, "a")
  f.write("Now the file has more content!")
  f.close()

load_page()

if st.button('next word'):
    refresher()
else:
    st.write('')
