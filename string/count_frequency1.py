#counting frequencys in a list using dictionary
fruits = ["apple", "banana", "apple", "cherry", "banana"]
count_words = {}
for words in fruits:
    count_words[words] = count_words.get(words, 0) + 1
    
print(count_words)