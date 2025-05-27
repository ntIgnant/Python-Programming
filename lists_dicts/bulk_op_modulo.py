list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

list3 = [p for i in list1, for j in list2, p = i * j]

print(list3)
