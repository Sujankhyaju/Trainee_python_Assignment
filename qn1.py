# Make a list of ten students in your class. Print the name of each student whose name starts with ‘B’.


std = list()
print("Enter name of 10 students in your class\n")
for i in range(1,11):
    name = input(f"{i} -->")
    std.append(name)

for name in std:
    if ord(name[0]) == 66:   #checks if the name starts with 'B'. Asci value of B is 66 and b is 98
        print(name)


