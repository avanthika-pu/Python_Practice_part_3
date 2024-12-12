#Python – Remove empty List from List
mylist = [10, [], 20, [], 30, [], 40]
for emp_list in mylist:
    if emp_list == []:
        mylist.remove(emp_list)
        pass
print(mylist)