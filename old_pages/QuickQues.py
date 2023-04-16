import streamlit as st
from pages.Utilities.Utilities import Questions, Utilities
from pathlib import Path
st.set_page_config(page_title="Quick Questions",
                   page_icon="🔢")

Questions.quick_questions("quick_code_ques.py",num_questoin=1)
