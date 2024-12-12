#Python | Count occurrences of an element in a list
#2.using counter
from collections import Counter
mylist = [1,2,1,3,2,4,3,5,3,2,1]
counter = Counter(mylist)
count_num = counter[1]

print("Count of i is:",count_num)