# 11.	Write a program to double a given number and add two numbers using lambda()?

def main():
    '''
    using lambda to double a number and add two numbers
    '''
    num = int(input("Enter a number: "))
    db = lambda num : num*2
    ad = lambda a,b : a+b
    print("twice value of {} is {} ".format(num,db(num)))
    print("Addition of 3 and 5 is ",ad(3,5))


if __name__ == '__main__':
    main()