import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'  # provides the key of the  text input label so that when the user
    # presses Enter in the text box, this function gets called and assigns a to-do to text was typed. session state is a
    # dictionary
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()
st.title("My Todo App")
st.subheader("This is my subheader")
st.write("This is app will make you a productivity genius")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) # needed to add the key value here so that the checkboxes can be accessed by
    # st.session_state. This will allow us to perfomr actions to the checkboxes
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]  # this is needed so you can delete the session state dictionary
        st.rerun()  # this is required for checkboxes, this rerun the script from the top aka the beginning

st.text_input("", placeholder="Enter a new todo...", key="new_todo",
              on_change=add_todo)  # the on_change calls the function add_todo
# st.session_state   # this code allows you to see whats inside the session state on the web application

