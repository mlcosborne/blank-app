import streamlit as st
st.subheader("Should I Practice Tool",divider = True)
number = st.select_slider("How many times did you want to practice this week?", [0,1,2,3,4,5,6,7])

if number < 3:
    st.write("Too low, aim higher")

alreadynumber = st.select_slider("How many times have you practiced already this week?", [0,1,2,3,4,5,6,7])
scales = st.pills("Have you practiced your scales", ["Yes", "No"])

if number - alreadynumber > 0:
    st.write("Practice more! The grind never stops!")
elif  number - alreadynumber <= 0 and scales == "No":
    st.write("Practice your scales, they are important!")
elif number - alreadynumber <= 0 and number != 0 or scales == "Yes":
    st.write("You don't need to practice, but you still could!")