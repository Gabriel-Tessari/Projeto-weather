import os
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI
from langchain.utilities import OpenWeatherMapAPIWrapper
import streamlit as st
from langchain.chat_models import ChatOpenAI
chat = ChatOpenAI()
from langchain.schema import HumanMessage, SystemMessage

os.environ["OPENWEATHERMAP_API_KEY"] = "bad342cd76758883d77cb1c00b013408"

st.title("WEATHER ADVISOR")
llm = OpenAI(temperature=0)

tools = load_tools(["openweathermap-api"], llm)

agent_chain = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

local = st.text_input('Local desejado', '')
pergunta = "Como está o tempo em " + local,'?'
bo = st.button("Checar o Tempo")

if bo:   
    a = agent_chain.run(pergunta)

    texto = "Qual a temperatura maxima em: " + a
    texto2 = "Qual a temperatura minima em: " + a
    texto3 = "Qual a temperatura atual em: " + a 
    b=chat(
        [
            HumanMessage(
                content= texto
            )
        ]
    )
    c = chat(
        [
            HumanMessage(
                content= texto2
            )
        ]
    )
    d = chat(
        [
            HumanMessage(
                content= texto3
            )
        ]
    )
    
    st.subheader(b)
    st.divider()
    st.subheader(c)
    st.divider()
    st.subheader(d)
    
    