import streamlit as st
import functions

TaskList = functions.get_tasks()


def add_todo():
    new_task = st.session_state["new task"] + "\n"
    TaskList.append(new_task)
    functions.write_tasks(TaskList)


st.title("My Todo App")
st.subheader("This is my app for managing tasks")
st.write("Using this app increases productivity by 69%")

for index, task in enumerate(TaskList):
    task.strip("\n")
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        TaskList.pop(index)
        functions.write_tasks(TaskList)
        del st.session_state[task]
        st.rerun()

st.text_input(label=" ", placeholder="Add new task here",
              on_change=add_todo, key="new task")


