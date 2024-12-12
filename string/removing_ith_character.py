#Python program for removing i-th character from a string
def remove_item(input_str, i):
    return input_str[:i] + input_str[i+1:]
    
i = 6
input_str = "pythonprogramming"
result = remove_item(input_str, i)
print(result)