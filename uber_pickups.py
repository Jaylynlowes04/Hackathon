import streamlit as st
import pandas as pd
import numpy as np
from langchain.llms import OpenAI
llm = OpenAI(openai_api_key="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")
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
llm = OpenAI(openai_api_key="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")
chat_model = ChatOpenAI(openai_api_key="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")


st.title('Chat with TroyAI')

question = st.text_input("Enter your Question","")
if(question):
    #Get answer from OpenAI
    #st.write that answer to the user
    response = chat_model.predict(question)
    st.write(response)
