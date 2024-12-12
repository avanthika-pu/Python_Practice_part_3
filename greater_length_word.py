# Find words which are greater than given length k
def greater_word(words, k):
    return [word for word in words if len(word)> k]

words_list = ['apple','banana','kiwi','grape','orange','peach']
k = 5
result =greater_word(words_list,k)
print(result)
