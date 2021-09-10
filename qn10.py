# 4.	Write a program to check whether the input alphabet is vowel or not using if-else.
# 5.	Write a program to check whether the entered year is leap year or not.
# 6.	Write a program to check if the number is Armstrong or not.

def main():
    '''
    check given alphabet is vowel or not
    '''
    vowel = ['a','e','i','o','u']
    inp = input("Enter an alphabet ")
    if inp in vowel:
        print("Vowel")
    else:
        print("non vowel")

if __name__ == '__main__':
    main()