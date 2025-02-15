#Home#

import streamlit as st

st.title(":exclamation: UNC Bassoon Studio Home :exclamation:")
st.subheader("Upcoming events", divider = True)
st.write("Bassoon Studio Recital on April 6th")

st.subheader("Past events", divider = True)
st.write("Dr. Kunttu Faculty Recital on February 7th")
st.video("https://www.youtube.com/watch?v=sMSQyXGoCfs")

st.subheader("Follow us on Instagram!", divider = True)
st.link_button("Instagram Link :camera_with_flash:", "https://www.instagram.com/uncbassoons/")

toggleon = st.toggle("Bassoon Mode?")
if toggleon:
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXY1enVwMXVwcWxsNWx5M3g0dHY3NDFwbXJqdzV2emk5OXIwZXhudSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPJPmbXMCq8035NWE/giphy.gif")