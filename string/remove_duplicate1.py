#remove duplicate using fromkeys
sentence = "python is easy, python is also simple"
print( ' '.join(dict.fromkeys(sentence.split())))
