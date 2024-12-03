import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo-app")
st.subheader("This is my todo app")
st.write("This app is to increase my productivity")

for index, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{index}")

st.text_input(label="", placeholder="Add new todo..")

print("Hello")