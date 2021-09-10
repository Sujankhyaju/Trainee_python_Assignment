#  Change the first alphabet of all elements of the following list to capital. 
#      Bob = [‘hurricane’,’tambourine’,’blowing’,’numb’]


def capName(list1):
    '''
    return capitalized names
    '''
    return [ i.capitalize() for i in list1 ]

def main():
    Bob = ['hurricane','tambourine','blowing','numb']
    print("Original List:",Bob)
    print("\nModified List:",capName(Bob))

if __name__ == '__main__':
    main()


