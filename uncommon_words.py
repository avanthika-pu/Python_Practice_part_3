#Python program to find uncommon words from two Strings
def uncommon_word(str1, str2):
    uncommon = []
    for word in str1:
        if word not in str2:
            uncommon.append(word)
            
    for word in str2:
        if word not in str1:
            uncommon.append(word)
    return uncommon
    
str1 = 'apple', 'orange', 'grape'
str2 = 'kiwi', 'blackberry', 'strawberry', 'apple'
print(uncommon_word(str1, str2))