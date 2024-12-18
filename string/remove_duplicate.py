#remove duplicate words from sentence
sentence = "python is simple, python is also easy"
split_sentence = sentence.split()
new_list = []
for words in split_sentence:
    if(sentence.count(words)>=1 and(words not in new_list)):
        new_list.append(words)
print(' '.join(new_list))        
