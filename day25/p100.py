# program to sort words by length
word=input("enter words: ").split()
word.sort(key=len)
print(word)
