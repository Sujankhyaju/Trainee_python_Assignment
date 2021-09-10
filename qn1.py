# Make a list of ten students in your class. Print the name of each student whose name starts with ‘B’.


def filterStudents(list1):
    '''
    shows the name of student whose name starts with 'B'
    '''
    for name in list1:
        if ord(name[0]) == 66:   #checks if the name starts with 'B'. Asci value of B is 66 and b is 98
            print(name)

def registerStudent():
    '''
    take names of students
    '''
    std = list()
    print("Enter name of 10 students in your class\n")
    for i in range(1,11):
        name = input(f"{i} -->")
        std.append(name)
    
    return std

def main():
    std = registerStudent()
    filterStudents(std)

    
if __name__ == '__main__':
    main()
