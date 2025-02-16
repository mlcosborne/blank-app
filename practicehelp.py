import streamlit as st
st.subheader("Should I Practice Tool", True)
number = st.chat_input("How many times did you want to practice this week, answer as a number?")

if number := st.chat_input("How many times did you want to practice this week, answer as a number?") and number < 3        
    messages.chat_message("user").write(number)
    messages.chat_message("assistant").write("Too low, aim higher")
 
if number := st.chat_input("How many times did you want to practice this week, answer as a number?"):
     messages.chat_message("user").write(number)
     messages.chat_message("assistant").write("Yes, practice more")