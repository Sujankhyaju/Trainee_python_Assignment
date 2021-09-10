# 4.	Write a program to check whether the input alphabet is vowel or not using if-else.
# 5.	Write a program to check whether the entered year is leap year or not.
# 6.	Write a program to check if the number is Armstrong or not.

vowel = ['a','e','i','o','u']
inp = input("Enter an alphabet ")

if inp in vowel:
    print("Vowel")

else:
    print("non vowel")


# 5.	Write a program to check whether the entered year is leap year or not.

inpt = int(input("Enter a year"))

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