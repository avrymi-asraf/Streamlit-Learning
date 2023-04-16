#1
my_list = [[],[1,1,1],["a","b","c"]]
lst = my_list[0]

print(lst)
#2
my_list = [[],[1,1,1],["a","b","c"]]
lst = my_list[1]

print(lst)
#3
my_list = [[],[1,1,1],["a","b","c"]]
num = my_list[1][1]

print(num)
#4
my_list = [[],[1,1,1],["a","b","c"]]
lst = my_list[2]

print(lst[2])
#5
my_list = [[],[1,1,1],["a","b","c"]]
lst = my_list[2]
char = lst[0]

print(char)
#6
my_list = [[],[1,1,1],["a","b","c"]]
ind = my_list[1][0]
char = my_list[ind][ind]

print(char)
#7
my_list = [[],[1,1,1],["a","b","c"]]
lst = my_list[0]
lst.append(my_list[1])

print(lst)
#8
my_list = [[],[1,1,1],["a","b","c"]]
lst = my_list[0]
lst.append(my_list[1][0])
lst.append(my_list[2][1])

print(lst)