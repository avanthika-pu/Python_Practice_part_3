#find anagram in string
def anagram_string(words):
    anagram_words={}
    for word in words:
        sorted_word = "".join(sorted(word))
        anagram_words.setdefault(sorted_word,[]).append(word)
    for group in anagram_words.values():
        print(group)  
        
words = ["listen", "silent", "enlist", "rat", "tar", "art", "evil", "vile", "live"]
print(anagram_string(words))