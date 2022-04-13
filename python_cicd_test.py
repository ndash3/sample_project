import os
list1 = [8,9,3,6,1,10]
list1.reverse()
print("The reverse list is {}".format(list1))

list2 = [97, 61, 120, 34, 76, 54, 78, 87, 56, 64, 345]
list2.sort()
print(f"The sorted list is {list2}")

list3 = []
list3 = list1.copy()
print("List3=", list3)

indexvalue = list2[2:6]
print("The index value are", indexvalue)