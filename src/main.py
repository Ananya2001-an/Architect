import streamlit as st

st.title("Welcome to Architect! :sparkles:")
st.text("Architect helps you quickly prototype and validate your ideas for hackathon projects.")

st.divider()

st.text_area(label='What is the functionality of your webapp? (both frontend and backend)', placeholder='Eg. Webapp that allows users to signup, search up a fundraiser and donate to it...')

st.text_area(label='What is your app\'s tech stack?', placeholder='OpenAI API, Streamlit, Javascript,...')

st.slider('How many members are there in your team?', 1, 5)

st.multiselect('What is your team\'s skill level?', ["beginner", "intermediate", "experienced"])

st.button(label='Generate Result')