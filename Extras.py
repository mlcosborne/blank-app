#Extras#
import streamlit as st
import pandas as pd

st.title("Extras")

instrumentlist = ["Clarinet","Flute", "Trumpet", "Violin", "French Horn", "Bassoon"]
choice= st.selectbox("What is the best Instrument?",instrumentlist)
if choice == instrumentlist[5]:
    st.write("Correct!")
else:
    st.write("WRONG TRY AGAIN")

data = {"Everyone Else": [200, 100, 20, 5, 0, -10, -20, -10, -30, -20],
    "Bassoons": [100, 150, 120, 180, 200, 220, 300, 350, 500, 600]}
dataframe = pd.DataFrame(data)

st.line_chart(dataframe)

left, middle= st.columns(2)
if left.button("bassoon??", use_container_width=True):
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWUxOG05ZXJsY2hsNXdjZnhlODR3cjBjN2Flc2QzZTdyZnY0aDdkeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fVo8zZXoZcxo5W8Z5W/giphy.gif")
    st.write("made by deblazers on giphy")
if middle.button("More bassoon?????", use_container_width=True):
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnoxYzl0MG5meHkyaG80YWplM2g3NnhqdDdma2hncTRqY3lycmg1NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/31PYcDl7J5cPCWvVNL/giphy.gif")
    st.write("made by grantkoltoons on giphy")