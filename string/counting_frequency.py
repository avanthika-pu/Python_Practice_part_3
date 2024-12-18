#counting frequencys in a list using dictionary
from collections import Counter
fruits = ["apple", "banana", "cherry", "banana", "apple", "guava","banana"]
count_of_words = Counter(fruits)
print(count_of_words)
