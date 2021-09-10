# Generate the following patterns using for loop
		
    # F
    # FFF
    # FFFFF
    # FFFFFFF
    # FFFFFFFFF
    # FFFFFFFFFFF
# ---------------------------------------------------
print("--------------Pattern #1--------------------------------")
n=1
for i in range(0,6):
    for j in range(0,n):
        print("F",end='')
    
    n+=2
    print("\r")


print("_____________Pattern #2_______________________________")
# ---------------------------------------------------
# F
# F
# FF
# FFF
# FFFFF
# FFFFFFFF
# FFFFFFFFFFFFF
# ------------------------------------------------

n1=0
n2=1

for i in range(0,7):
    for j in range(0,n2):
        print("F",end='')

    n3 = n2+n1
    n1 = n2
    n2 = n3
    
    print('\r')
