#Python – Replace multiple words with K
first_str = "which one is simple , python and cs"
print("original string is:" +str(first_str))
word_list=["simple", "python", "and"]
replaced_word = "spa"
result = ' '.join([replaced_word if word in word_list else word for word in first_str.split()])
print("string after multiple replace:"+str(result))