def deleteDuplicates(array:list) -> list:
    array=set(array)
    array=list(array)
    return array

list1=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4]
print(deleteDuplicates(list1))
