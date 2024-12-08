# Python | Check if a given string is binary string or not
def binary_str(str1):
    for elements in str1:
        if elements == '0' or elements == '1':
            return elements
    return None

str1 = 'python1'
print(binary_str(str1))