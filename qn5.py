# Write a Python function to multiply all the numbers in a list.


def multiplication(list1):
    '''
    multiply all the numbers in a list
    '''
    result = 1
    for i in list1:
        result = result * i
    
    return result

def main():
    list1 = [2,3,4,5,6,7,8,9]
    print("Multiplication of all the numbers in a list is :",multiplication(list1))

if __name__ == '__main__':
    main()
