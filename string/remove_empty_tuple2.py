#Python | Remove empty tuples from a list
#1. remove() method
mylist = [(1,2),(),(3,4),(),(5,6),()]
for emp_tuple in mylist:
    if emp_tuple == ():
        mylist.remove(emp_tuple)

print(mylist)