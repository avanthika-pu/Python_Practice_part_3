#Python | Count occurrences of an element in a list
#1.using loop
mylist = [1,2,3,1,2,4,5,1,2,4,5]
element = 1
count = 0
for item in mylist:
    if item == element:
        count += 1
print("Count of 1 is:", count)