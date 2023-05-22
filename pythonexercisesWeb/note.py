#

def listFunc(array:list):
    sum=0
    for item in range(len(array)):
        if not isinstance(item,int):
            print("list contains invalid values")
            sys.exit()
        sum+=item
    return sum

def listFuncv2(array:list):
    if all(isinstance(i,array) for i in array):
        return sum(array)
    else:
        #raise ValueError("list contains other than int")
        #אופציה נוספת שאפשר להשתמש בה אך היא אכן תחזיר שגיאה, לכן אני אישית מעדיף לא להשתמש בזה.
        sys.exit()


import re

