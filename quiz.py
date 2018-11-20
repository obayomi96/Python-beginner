score = 0

print("1. How many out of school centers does codelagos have? \n")
print(" a. 4\n b. 12\n c. 21 \n d. 30 \n Type your answer below")
answer1 = input("= ")
if(answer1 == "c" or answer1 == "21"):
    score += 1
    print("Correct")
else:
    print("Wrong")

print("2. In what year did codelagos start? \n")
print(" a. 2017\n b. 2012\n c. 1999 \n d. 2018 \n Type your answer below")
answer2 = input("= ")
if(answer2 == "a" or answer2 == "2017"):
    score += 1
    print("Correct")
else:
    print("Wrong")
    
print("3. How many lagoscian doescodelagos intend to train by 2020? \n")
print(" a. 1,000,000\n b. 2,000,000\n c. 3,000,000 \n d. 4,000,000 \n Type your answer below")
answer3 = input("= ")
if(answer3 == "a" or answer3 == "1,000,000"):
    score += 1
    print("Correct")
else:
    print("Wrong")

print("Your score is "+str(score))
