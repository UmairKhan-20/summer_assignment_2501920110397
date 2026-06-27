# program to find longest word
s=input("enter a string: ")
longest=""
for word in s.split():
    if len(word)>len(longest):
        longest=word
print("longest word is: ",longest)
                                                                                                                                                                                                 