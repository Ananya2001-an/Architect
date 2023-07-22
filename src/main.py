import streamlit as st

st.title("Welcome to Architect! :sparkles:")
st.text("Architect helps you quickly prototype and validate your ideas for hackathon projects.")

st.divider()

st.text_area(label='How your app should look?', placeholder='Eg. Webapp that allows users to signup, search up a fundraiser and donate to it...')

st.multiselect('What is your app\'s tech stack?', ["javascript", "react", "firebase", "python", "java", "git", "css", "azure", "aws", "nodejs", "flask", "fastapi", "sql", "mongodb", "nosql", "appwrite", "machine learning"])

st.slider('How many members are there in your team?', 1, 5)

st.multiselect('What are your team\'s skills?', ["javascript", "react", "firebase", "python", "java", "git", "css", "azure", "aws", "nodejs", "flask", "fastapi", "sql", "mongodb", "nosql", "appwrite", "machine learning"])

st.number_input('What is the hackathon deadline?', 0, 200)

st.button(label='Generate Result')