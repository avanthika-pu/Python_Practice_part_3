#Python | Remove empty tuples from a list
#2.list comprehension
mylist = [(1,2),(),(3,4),(),(5,6),()]
res_list = [item for item in mylist if item]

print("resultant list :",res_list)