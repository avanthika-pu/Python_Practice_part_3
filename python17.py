#Python – Replace duplicate Occurrence in String
text = "This is python program, python is simple"
words = text.split() 
repeated = [] 
new_text = [] 

for word in words:
    if word not in repeated:
        repeated.append(word)  
        new_text.append(word)   
    else:
        new_text.append("Replacement")  

final_text = ' '.join(new_text)  
print(final_text)

        