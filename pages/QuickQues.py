import streamlit as st
from __init__ import Questions, Utilities, QuickQuestions
from pathlib import Path

st.set_page_config(page_title="Quick Questions", page_icon="🔢",initial_sidebar_state="collapsed")
QuickQuestions("cods_questions/quick_ques_function.py",seconds=3, num_questoin=1)

