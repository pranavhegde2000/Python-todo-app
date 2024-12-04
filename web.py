import streamlit as st
import functions
#The flow of the code will be from top to bottom, line by line
todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("My Todo-app")
st.subheader("This is my todo app")
st.write("This app is to increase my productivity")

for index, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{index}")

st.text_input(label="", placeholder="Add new todo..",
              on_change=add_todo, key='new_todo')

print("Hello")
