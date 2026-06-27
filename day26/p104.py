# program to create quiz application
score = 0
print("      Welcome to the Quiz Application       ")
print("Question 1: What is the capital of germany?")
answer = input("Enter your answer: ")
if answer.lower() == "berlin":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")
print("Question 2: Who is the president of india presently?")
answer = input("Enter your answer: ")
if answer.lower() == "droupadi murmu":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")
print("Question 3: What is the currency of japan?")
answer = input("Enter your answer: ")
if answer.lower() == "yen":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")
print("Question 4: What is the largest ocean in the world?")
answer = input("Enter your answer: ")
if answer.lower() == "pacific ocean":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")
print("Question 5: Who is the founder of microsoft?")
answer = input("Enter your answer: ")
if answer.lower() == "bill gates":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")
print("Question 6: Who is the CEO of SPACEX?")
answer = input("Enter your answer: ")
if answer.lower() == "elon musk":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")
print("Question 7: What is the capital of pakistan?")
answer = input("Enter your answer: ")
if answer.lower() == "islamabad":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer.")
print("Your total score is:", score)