# Python | Check if a given string is binary string or not
def binary_str(str1):
    bin_digit = [value for value in str1 if value == '0' or value == '1']
    return bin_digit[0]if bin_digit else None
str1 = 'python1program'
print(binary_str(str1))