# 3.	users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
#         'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
#         'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}
# Generate a list of usernames, name, age and poison from the above dictionary.


def Usernames(users):
    return list(users.keys())

def Names(users):
    names = [ i['name'] for i in users.values() ]
    return names

def Ages(users):
    ages = [i['age'] for i in users.values()]
    return ages

def Poisons(users):
    poisons = [ i['poison'] for i in users.values()]
    return poisons

def main():
    users = {
        'g91':{'name':'Aron','age':55,'poison':'Old monk'},
        'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
        'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}
        }
        
    print("\nUSERNAMES:: ",Usernames(users))  
    print("\nNAMES:: ",Names(users))
    print("\nAges:: ",Ages(users))
    print("\nPOISONS:: ",Poisons(users))      


if __name__ == '__main__':
    main()