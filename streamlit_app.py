import streamlit as st

#making different tabs#
pages = st.navigation([st.Page("Home.py"),st.Page("Recordings.py"),st.Page("PracticeHelp.py"),st.Page("Extras.py")])
pages.run()


