import Page_1
import Page_2
import streamlit as st

st.set_page_config(
    page_title="NHTSA Crash Case Analysis",
    page_icon="",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://discuss.streamlit.io/',
        'Report a bug': "https://github.com/streamlit/streamlit/issues/new/choose",
        'About': ""
    }
)

PAGES = {'Data Visualization': Page_1,
         'Statistical Analysis': Page_2}

st.sidebar.title ('Menu')
selected = st.sidebar.selectbox ('Select Page: ', ['Data Visualization', 'Statistical Analysis'])

page = PAGES [selected]

page.app ()