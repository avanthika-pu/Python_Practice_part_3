#counting frequencys in a list using dictionary
from collections import defaultdict
fruits = ["apple", "banana", "cherry", "apple", "banana", "mago"]
count_of_words = defaultdict(int)
for words in fruits:
    count_of_words[words] += 1
    
print(dict(count_of_words))

