import streamlit as st
import asyncio
import json
from langchain.chat_models import ChatOpenAI
from backend_chain import backend_chain
import dotenv
dotenv.load_dotenv()

llm = ChatOpenAI(temperature=0, max_tokens=1000, model="gpt-3.5-turbo")
advanced_llm = ChatOpenAI(temperature=0, max_tokens=1000, model="gpt-4")

async def get_backend_results():
    output = await backend_chain(inputs = {
        'project_details': project_details,
        "project_technologies": project_technologies,
        "group_size": group_size,
        "group_experience": group_experience
    },
    llm=llm,
    advanced_llm=advanced_llm)
    output_json = json.loads(output)
    if output_json["approval"] == "1":
        st.success('Approved! This project is feasible according to the hackathon time period.', icon="✅")
    else:
        st.error('Not approved! This project is not feasible according to the hackathon time period.', icon="🚨")

        with st.container():
            st.text('Comments 👇')
            st.info(output_json["comments"], icon="ℹ️")


async def run_tasks():
    task1 = asyncio.create_task(get_backend_results())
    # task2 = asyncio.create_task(async_function2())

    # wait for both tasks to complete
    await task1
    # await task2

st.title("Welcome to Architect! :sparkles:")
st.text("Architect helps you quickly prototype and validate your ideas for hackathon projects.")

st.divider()

project_details = st.text_area(label='What is the functionality of your webapp? (both frontend and backend)', placeholder='Eg. Webapp that allows users to signup, search up a fundraiser and donate to it...')

project_technologies = st.text_area(label='What is your app\'s tech stack?', placeholder='OpenAI API, Streamlit, Javascript,...')

group_size = st.slider('How many members are there in your team?', 1, 5)

group_experience = st.radio('What is your team\'s skill level?', ["beginner", "intermediate", "experienced"])

result = st.button(label='Generate Result')

if result:
    with st.spinner('Calculating...'):
        asyncio.run(run_tasks())
