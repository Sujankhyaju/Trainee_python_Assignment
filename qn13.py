# 5.	Write a program to check whether the entered year is leap year or not.

def main():
    '''
    take year input and check if LEAP Year
    '''
    inpt = int(input("Enter a year:: "))
    if inpt % 4 == 0:
        if inpt % 100 ==0:
            if inpt % 400 == 0:
                print("LEAP YEAR")
            else:
                print("Not LEAP Year")
        else:
            print("LEAP YEAR")
    else:
        print("NOT LEAP YEAR")


if __name__ == '__main__':
    main()