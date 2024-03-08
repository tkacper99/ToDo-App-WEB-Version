import streamlit as st
import os
import functions

if not os.path.exists("data.txt"):
    with open("data.txt", "w")as file:
        pass

todos = functions.get_todos()

st.title("Todo App")
st.subheader("Max your productivity")
st.write("This todo app is written in Python using the streamlit library")

for todoItem in todos:
    st.checkbox(todoItem)

st.text_input(label="", placeholder="Add new todo...")