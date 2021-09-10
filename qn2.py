#  Change the first alphabet of all elements of the following list to capital. 
#      Bob = [‘hurricane’,’tambourine’,’blowing’,’numb’]


print("---------------------LIST--------------\n")
Bob = ['hurricane','tambourine','blowing','numb']

print("Original List:",Bob)

for i in range(len(Bob)):
    Bob[i] = Bob[i].capitalize()

print("Modified List:",Bob,'\n\n')

print("-------------------DICTIONARY--------------------------\n")

# 3.	users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
#         'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
#         'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}
# Generate a list of usernames, name, age and poison from the above dictionary.

users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
        'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
        'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}
        }

usernames = list(users.keys())
names = [ i['name'] for i in users.values() ]
ages = [i['age'] for i in users.values()]
poisons = [ i['poison'] for i in users.values()]
print("USERNAMES",usernames)  
print("NAMES",names)
print("Ages",ages)
print("POISONS",poisons)      


