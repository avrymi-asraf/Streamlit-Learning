import sys
import os
import streamlit as st
import pandas as pd
import numpy as np
from __init__ import WriteAnswers, Questions, Utilities, DataLoader
names_df: DataLoader = DataLoader("names_and_answers/names.csv")
status_df: DataLoader = DataLoader("names_and_answers/answers_ex1.csv")

st.set_page_config(page_title="Functions", page_icon="🔢")

name = Utilities.enter_name(names_df)
Utilities.first_time_message(
"""# חשוב מאוד
שימו לב האם הפונקציה צריכה להחזיר משהו, ואת מה בדיוק היא צריכה להחזיר
או שהפונקציה צריכה להדפיס משהו ולא להחזיר
""")
write_answers: WriteAnswers = WriteAnswers(name, status_df)
st.title(f"{name} Welcome to Ex1")
st.dataframe(
    status_df.df.loc[status_df.df["NAME"] == name].replace([np.nan, " "], "🤔"),
    use_container_width=True,
)

Questions.execute_question(
    1,
    """
    Create a function that takes a number as an input and __returns__ the square of that number
    """,
    code="""def square(num):\n\tpass\n\n\n\nprint(square(5)) # prints 25""",
    write_answer=write_answers,
    caption="""צור פונקציה שלוקחת מספר כקלט ומחזירה את הריבוע של המספר הזה""",
)

Questions.execute_question(
    2,
    """
    Create a function that takes two numbers as input and __print__ the sum of those numbers.
    """,
    code="""def add(num1, num2):\n\tpass\n\n\n\nadd(5, 10) # prints 15""",
    write_answer=write_answers,
    caption="""צור פונקציה שלוקחת שני מספרים כקלט __ומדפיסה__ את סכום המספרים הללו.""",
)
Questions.execute_question(
    3,
    """
    Create a function that takes a list of numbers as input and __returns__ the average of those numbers.
    Reminder: Average is the sum of the members divided by the number of members
    """,
    code="""def average(numbers):\n\tpass\n\n\n\nprint(average([1, 2, 3, 4, 5])) # prints 3.0""",
    write_answer=write_answers,
    caption="""צור פונקציה שלוקחת רשימה של מספרים כקלט __ומחזירה__ את הממוצע של המספרים הללו.
    תזכורת: ממוצע הוא סכום האברים לחלק למספר האיברים
    """,
)
Questions.execute_question(
    4,
    """
Create a function that __prints__ all the objects in the list, one by one not together, use a for loop. the function returns nothing
    """,
    code="""def print_list(lst):\n\tpass\n\n\n\nprint_list(["a", 2, [], 4,5,6])""",
    write_answer=write_answers,
    caption="""צרו פונקציה שמדפיסה את כל המספרים ברשימה, אחד אחד לא ביחד
    """,
)
Questions.execute_question(
    5,
    """
Create a function that accepts a number as an argument, if it is even __returns__ true else returns false
    """,
    code="""def is_even(num):\n\tpass\n\n\n\nprint(is_even(3)) #print false\nprint(is_even(4)) #print true""",
    write_answer=write_answers,
)
Questions.execute_question(
    6,
    """
Copy the previous function into the current code.
Create a function that takes a number as input and __print__ "even" if the number is even and "odd" if the number is odd. 
Use the `is_even` function from the previous section
    """,
    code="""def is_even(num):\n\tpass\n\ndef even_or_odd(num):\n\tpass\n\n\n\neven_or_odd(89) # prints odd\neven_or_odd(222) # prints even""",
    write_answer=write_answers,
)
Questions.execute_question(
    7,
    """
Copy the function from section 3 into the current code.
Create a function that goes through all the numbers in the list and prints all the numbers that are greater than the average,
use a for loop, and the function from section 3
    """,
    code="""def average(numbers):\n\tpass\n\ndef print_larger_average(numbers):\n\tpass\n\n\n\nprint_larger_average([1, 2, 3, 4, 5,6]) # prints 4,5,6""",
    write_answer=write_answers,
    caption="""העתיקו את הפונקציה הקודמת לתוך הקוד הנוכחי. 
צרו פונקציה שעוברת על כל המספרים ברשימה ומדפיסה את כל המספרים שגדולים מהממוצע, השתמשו בלולאת פור, ובפונקציה מסעיף 3
    """,
)
