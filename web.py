import streamlit as st
import functions

# The flow of the code will be from top to bottom, line by line
todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    # session_state is used to save info on all the widgets in the web app, it is stored in key value pairs, info regarding newtodo and and the existing todos are all added
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo-app")
st.subheader("This is my todo app")
st.write("This app is to increase my productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"Todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"Todo_{index}"]
        st.rerun()  # this will rerun the web app,so we dont have to refresh to see if the checked todo item is removed or not

st.text_input(label="", placeholder="Add new todo..",
              on_change=add_todo, key='new_todo')

print("Hello")
