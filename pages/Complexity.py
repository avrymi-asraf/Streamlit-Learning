import sys
import os
import streamlit as st
import pandas as pd
import numpy as np
from streamlit import session_state as ses
from __init__ import WriteAnswers, Questions, Utilities, DataLoader

names_df: DataLoader = DataLoader("names_and_answers/names.csv")
status_df: DataLoader = DataLoader("names_and_answers/answers_ex1.csv")

st.set_page_config(
    page_title="Complexity", page_icon="🔢", initial_sidebar_state="collapsed"
)

name = Utilities.enter_name(names_df)
write_answers: WriteAnswers = WriteAnswers(name, status_df)
st.title(f"{name} Welcome to Ex1")
st.dataframe(
    status_df.df.loc[status_df.df["NAME"] == name].replace([np.nan, " "], "🤔"),
    use_container_width=True,
)

st.write("""
The variable is always `n` or `m`,
If you need to add constants, use a plus sign, `+`
If multiplying by a constant, use the multiplication sign `*`
If you need to specify a predicate, use `**`

You won't always need to use the time measurement
""")
Questions.regular_question(
    "q1",
    1,
    """
    What is the runtime of this function?
    """,
    "n",
    code="""
import time
    
def f1(n):
    for i in range(n):
        do_something()

start  = time.time()
f1(1000)
end = time.time()
""",
    write_answer=write_answers,
    code_add_before="""import time
do_something = lambda : time.sleep(0.0001)
    """,
)
Questions.regular_question(
    "q2",
    2,
    """
    What is the runtime of this function?
    """,
    "n",
    code="""
import time
Mysterious_function(100)
""",
    write_answer=write_answers,
    code_add_before="""
import time
do_something = lambda : time.sleep(0.001)
def Mysterious_function(n):
    for i in range(n):
        do_something()
""",
)
Questions.regular_question(
    "q3",
    3,
    """
    What is the runtime of this function?
    """,
    "n*3,3*n",
    code="""
import time
    
def f1(n):
    for i in range(3*n):
        do_something()

start  = time.time()
f1(1000)
end = time.time()
""",
    write_answer=write_answers,
    code_add_before="""import time
do_something = lambda : time.sleep(0.0001)
    """,
)


Questions.regular_question(
    "q4",
    4,
    """
    What is the runtime of this function?
    """,
    "n+2,2+n",
    code="""
import time
    
def f1(n):
    do_something()
    do_something()
    for i in range(n):
        do_something()

""",
    write_answer=write_answers,
    code_add_before="""import time
do_something = lambda : time.sleep(0.00001)
    """,
)
Questions.regular_question(
    "q5",
    5,
    """
    What is the runtime of this function?
    """,
    "n+m,m+n",
    code="""
import time
    
def f(n,m):
    for i in range(n):
        do_something()
    for i in range(m):
        do_something()

""",
    write_answer=write_answers,
    code_add_before="""import time
do_something = lambda : time.sleep(0.001)
    """,
)
Questions.regular_question(
    "q6",
    6,
    """
    What is the runtime of this function?
    """,
    "n**2,n*n",
    code="""
import time
    
def f1(n):
    for i in range(n):
        for j in range(n):
            do_something()

""",
    write_answer=write_answers,
    code_add_before="""import time
do_something = lambda : time.sleep(0.00001)
    """,
)
Questions.regular_question(
    "q7",
    7,
    """
    What is the runtime of this function?
    """,
    "n**2,n*n",
    code="""
import time
Mysterious_function(100)
""",
    write_answer=write_answers,
    code_add_before="""import time
do_something = lambda : time.sleep(0.001)
def Mysterious_function(n):
    for i in range(n*n):
        do_something()
    """,
)
Questions.regular_question(
    "q8",
    8,
    """
    What is the runtime of this function?
    """,
    "n*m,m*n",
    code="""
import time
    
def f(n):
    for i in range(n):
        for j in range(m):
            do_something()

""",
    write_answer=write_answers,
    code_add_before="""import time
do_something = lambda : time.sleep(0.0001)
    """,
)
Questions.regular_question(
    "q9",
    9,
    """
    What is the runtime of this function?
    """,
    "n*m**2,m**2*n",
    code="""
import time
Mysterious_function(100)
""",
    write_answer=write_answers,
    code_add_before="""import time
do_something = lambda : time.sleep(0.001)
def Mysterious_function(n,m):
    for i in range(m*m):
        for j in range(n):
            do_something()
    """,
)
