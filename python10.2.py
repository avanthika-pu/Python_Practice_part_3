#Python | Remove empty tuples from a list
#3.using lamda()method
mylist = [(1,2),(),(3,4),(),(5,6),()]
res_list = list(filter(lambda x: x!=(), mylist))

print('resultant list is:',res_list)