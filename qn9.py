# 7.	Write a program to compute the grade from marks. 

# Marks	Grade
# Marks<=50	F
# 60>=marks>50	E
# 70>= marks > 60	D
# 80>= marks > 70	C
# 90 > = marks > 80	B
# 100>= marks >90	A

def main():
    marks = int(input("Enter a marks:"))

    if marks <=50:
        print(f"Marks {marks} equivalent to Grade 'F'.")

    elif marks > 50 and marks <=60:
        print(f"Marks {marks} equivalent to Grade 'E'")

    elif marks > 60 and marks <=70:
        print(f"Marks {marks} equivalent to Grade 'D'")

    elif marks > 70 and marks <=80:
        print(f"Marks {marks} equivalent to Grade 'C'")

    elif marks > 80 and marks <=90:
        print(f"Marks {marks} equivalent to Grade 'B' ")

    elif marks > 90 and marks <=100:
        print(f"Marks {marks} equivalent to Grade 'A'")

    else:
        print('Invalid')


if __name__ == '__main__':
    main()