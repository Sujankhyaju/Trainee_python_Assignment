# 5.	A = [‘a’,’b’,’c’,’d’] B = [‘1’,’a’,’2’,’b’]
# Find  (A union B) and (A intersection B)

# c = list(set(A+B))
# d = [item for item in A if item in B]
# # for item in A:
# #     if item in B:
# #         d.append(item)
# print("The intersection of A and B is", d)


def main():
    A = ['a','b','c','d'] 
    B = ['1','a','2','b','c']
    print("The Union of A and B is", list(set(A)|set(B))) # Using logical OR operator
    print("The intersection of A and B is", list(set(A) & set(B))) #Using logical And operator


if __name__ == '__main__':
    main()