import sys
import os
import streamlit as st
import pandas as pd
import numpy as np
from pages.Utilities.Utilities import WriteAnswers, Questions, Utilities, DataLoader

names_df: DataLoader = DataLoader("names.csv")
status_df: DataLoader = DataLoader("answers_ex1.csv")

st.set_page_config(page_title="Ex1", page_icon="🔢")
name = Utilities.enter_name(names_df)
write_answers: WriteAnswers = WriteAnswers(name, status_df)
st.title(f"{name} Welcome to Ex1")
st.dataframe(
    status_df.df.loc[status_df.df["NAME"] == name].replace([np.nan, " "], "🤔"),
    use_container_width=True,
)

Questions.execute_question(
    1,
    "Printing the elements of a list of strings:",
    code='my_list = ["apple", "banana", "cherry"]',
    write_answer=write_answers,
)

Questions.execute_question(
    2,
    "Printing the to the power of 2 every number of a list of numbers:",
    code="my_list = [1, 2, 3, 4, 5]",
    write_answer=write_answers,
)

Questions.execute_question(
    3,
    "Printing the elements of my_list[0]:",
    code="my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]",
    write_answer=write_answers,
)
Questions.execute_question(
    4,
    "Printing the all elements of a list of lists:",
    code="my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]",
    caption="""הדפיסו את כל האברים בתוך כל הרשימות""",
    write_answer=write_answers,
)
Questions.execute_question(
    5,
    "Printing the elements of a string one character at a time",
    code='my_string = "Hello, world!"',
    caption="""הדפיסו אות אחת בכל פעם""",
    write_answer=write_answers,
)
Questions.execute_question(
    6,
    "Printing the elements of a string one character at a time, but not spaces",
    code='my_string = "Hello, world!"',
    caption=""" הדפיסו אות אחת בכל פעם ללא התו רווח השתמשו בתנאי כדי לבדוק האם להדפיס""",
    write_answer=write_answers,
)
