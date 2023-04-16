import sys
import os
import streamlit as st
import pandas as pd
import numpy as np
from pages.Utilities.Utilities import WriteAnswers, Questions, Utilities, DataLoader

names_df: DataLoader = DataLoader("names.csv")
status_df: DataLoader = DataLoader("answers_multi.csv")

st.set_page_config(page_title="Multiplication table", page_icon="🔢")
name: str = Utilities.enter_name(names_df)
write_answers: WriteAnswers = WriteAnswers(name, status_df)
st.title(f"{name} Welcome to Multiplication table Ex")
st.dataframe(
    status_df.df.loc[status_df.df["NAME"] == name].replace([np.nan, " "], "🤔"),
    use_container_width=True,
)

Questions.execute_question(
    1,
    """Printing the numbers 1 through 10: 
     _remember_ `range(x,y)` run from x to y-1""",
    write_answer=write_answers,
)


Questions.execute_question(
    2,
    """Print the numbers from 1-10 in one line, use the function `print_row()` a we provided you.
This function prints all the numbers in a row
""",
    code="""
print_row = lambda x: print(x,end=" ") 

#You should delete this example
print("hello")
print("world")

print_row("hello") 
print_row("world")
""",
    write_answer=write_answers,
)


Questions.execute_question(
    3,
    """Print the numbers $1*3$ to $10*3$ in one line
```python
3 6 12 ...
``` """,
    code="""print_row = lambda x: print(x,end=" ")
                           """,
    write_answer=write_answers,
)


Questions.execute_question(
    4,
    """Take the loop from the previous exercise and place it inside a loop that ran 3 times, so that it will be printed 3 times,use for in for
```python
3...30 3 ... 30 3...30 
```
""",
    code="""print_row = lambda x: print(x,end=" ")
                           """,
    write_answer=write_answers,
)


Questions.execute_question(
    5,
    """Copy the previous loop, and add `print()' after the outer loop. 
This command will print a new line, so you get
```python
3 6 9 ...30 
3 6 9 ...30 
3 6 9 ...30 
```
""",
    code="""print_row = lambda x: print(x,end=" ")""",
    caption="""העתיקו את הלולאה הקודמת, והוסיפו אחרי הלולאה החיצונית `print()` הפקודה הזאת תדפיס שורה חדשה, כך שתקבלו """,
    write_answer=write_answers,
)


Questions.execute_question(
    6,
    """Copy the previous code, now instead of multiplying by the constant number 3 use an ascending index,
 in the first round print$1...10$ in in the second round print $3 ... 30$ So until the whole multiplication table is printed""",
    code="""print_row = lambda x: print(x,end=" ")""",
    caption="""
                                        השתמשו בקוד הקודם, כעת במקום להכפיל כל מספר ב3 הכפילו אותו באינדקס עולה
                                        1-10   כך שבשורה הראשנה יודפס 
                                        `1... 10` בשורה השניה 
                                        `2 ... 20` וכן הלאה עד שיודפס כל לוח הכפל""",
    write_answer=write_answers,
)
