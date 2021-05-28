import streamlit as st
import datetime
import requests
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

date = st.date_input("Pickup date", datetime.date(2019, 7, 6))
formatted_pickup_datetime = date.strftime("%Y-%m-%d %H:%M:%S")

plongitude = st.number_input('pickup longitude')
platitude = st.number_input('pickup latitude')
dlongitude = st.number_input('dropoff longitude')
dlatitude = st.number_input('dropoff latitude')

pcount = st.number_input('passenger count')
pcount = int(pcount)


if st.button('Get Pred!'):
    params = {
        "pickup_datetime": formatted_pickup_datetime,
        "pickup_longitude": plongitude,
        "pickup_latitude": platitude,
        "dropoff_longitude": dlongitude,
        "dropoff_latitude": dlatitude,
        "passenger_count": pcount
    }

    url = 'https://taxifare.lewagon.ai/predict'
    response = requests.get(
        url,
        params=params,
    ).json()

    st.write(response['prediction'])





if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

number = st.number_input('Insert a number')
st.write(number)

d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )
'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
