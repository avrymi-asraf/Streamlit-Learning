##4
def first_num(name:str):
    for char in name:
        if char.isdigit():
            return  char
    return False

print(first_num("Eliran345 was here"))


