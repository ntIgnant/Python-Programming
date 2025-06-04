#print(len(0))
#print(len(""))

#a = 5
#b = 5

#c = [1, 2, 3]
#d = [1, 2, 3]

#print(a == b)
#print(a is b)
#print("")
#print(c == d)
#print(c is d)

#l = [i % 4 for i in range(10) if i % 3]
#print(l)

#p = [i % 2 for i in range(10) if i % 3]
#print(p)

#j = [i for i in "abac"]
#print(j)

#set_j = set(j)
#print(set_j)

# Get the median of an odd progresion?
mi_lista = [1, 5, 2, 4, 1, 6, 3]
sorted_lista = sorted(mi_lista) # sort the list

print(sorted_lista) # DEBUG

# Now, I should get the term in the middle
len_lista = len(sorted_lista)

mid_index = (len_lista // 2) + 1 # perform integer divison and then add one to get the follow-up value

median = sorted_lista[mid_index - 1]

print(median)
