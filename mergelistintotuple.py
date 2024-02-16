lst1 = [1,2,3,4,5,6]
lst2=['a','b','c','d','e','f']
new_list = [(lst1[i], lst2[i]) for i in range(0, len(lst1))]

print(new_list)