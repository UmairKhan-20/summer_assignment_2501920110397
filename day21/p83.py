# (vowels+consonants) count program
s=input("Enter a String: ")
vowels=0
consonants=0
for ch in s:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            vowels+=1
        else:
            consonants+=1
print("Vowels: ",vowels)
print("Consonants: ",consonants)