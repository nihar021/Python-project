print("welcome to my quiz!")
score=0
playing=input('DO you want to play? ')

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
print("For every question you will get 10 if guess correctly and get -5 if guess wrong")

answer=input("What does CPU stands for? ")
if answer.lower()=="central processing unit":
    print ('Correct!')
    score+=10
else:
    print("Incorrect!")
    score-=5

answer=input("What does GPU stands for? ")
if answer.lower()=="graphics processing unit":
    print ('Correct!')
    score+=10

else:
    print("Incorrect!")
    score-=5

answer=input("What does RAM stands for? ")
if answer.lower()=="random access memory":
    print ('Correct!')
    score+=10
else:
    print("Incorrect!")
    score-=5


answer=input("What does PSU stands for? ")
if answer.lower()=="power supply":
    print ('Correct!')
    score+=10

else:
    print("Incorrect!")
    score-=5

print("You have scored ",score)
