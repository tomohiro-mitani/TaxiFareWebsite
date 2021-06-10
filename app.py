import streamlit as st
from streamlit import caching
import requests
import os
import time

'''
# Welcome to our Flashcards app!
'''
'''
We prepared ten flashcards for you to learn/practice Japanese words.
'''
'''
Type your guess meaning of the Japanese word into the box below and click the ‘Check answer’ button to check.
'''
'''
Click on ‘Next word’ for more flashcards.
'''


def random():
  url = 'https://n1-flashcards-api.herokuapp.com/random'
  response = requests.get(
      url
  ).json()
  return  response

# def check_state():
#   url = 'http://localhost:8000/state'
#   response = requests.get(
#       url
#   ).json()
#   return  response

# def lookup():
#   url = 'http://localhost:8000/lookup'
#   response = requests.get(
#       url
#   ).json()
#   return  response

# def update_t():
#   url = 'http://localhost:8000/update_t'
#   response = requests.get(
#       url
#   ).json()
#   return  response

# def update_f():
#   url = 'http://localhost:8000/update_f'
#   response = requests.get(
#       url
#   ).json()
#   return  response

# def save(keyword):
#   url = f'http://localhost:8000/save/{keyword}'
#   response = requests.get(
#       url
#   ).json()
#   return  response

def load_page():
  response = random()
  st.write("Japanese word: ", response["word-jp"])
  st.text_input('What does this mean?', 'Write your answer here.')

  if st.button('Check the answer'):
      st.write(response["word-en"])
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


'''
Cards are predicted by our model, so there might be some spelling mistakes.
'''

'''
To learn more about how this flashcards app was made, please see the link below.
'''
st.write("[Link to slides](https://docs.google.com/presentation/d/1y3xZhCEnR-6-0CmB4evfgnobaNWRze0KVM77cb7fjYk/edit?ts=60becbb6#slide=id.gdbed1b9726_0_128)")


