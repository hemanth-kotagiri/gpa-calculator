import os

"""First, we got to get the credits in a dictionary"""
# Creating the dictionary for first semester with credits and subjects

os.system("cls")
totalCredits = 21

choicesDict = dict()

grades = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "F": 0}

subjectsAndCredits = {"COSM": 4, "Analog and Digital Electronics Theory": 3, "Data Structures Theory": 4,
                      "COA Theory": 3, "C++ Theory": 2, "ADE-LAB": 1, "DS-LAB": 1.5, "IT-LAB": 1.5, "C++ LAB": 1}


totalScore = 0

name = input("Well, what's you're name, buddy?\n").capitalize()
print("Hello %s, I see that you are very interested in knowing your GPA." %name)
print("Make sure that you type in your Grade in integers(0,5..10) or in alphabets(f,c,b..a+,o). Both will work fine.")
countForStupid = 0
countForFailure = 0

for everySubject in subjectsAndCredits:
    if countForStupid == 1:
        print("\nYou are a stupid.")
        break
    else:
        grade = input("\nWhat's your grade for {}: ".format(
            everySubject)).upper()
        if grade in grades.keys():
            if grade==0 or grade=="F":
                countForFailure+=1
            totalScore += grades[grade]*subjectsAndCredits[everySubject]
        else:
            try:
                if int(grade) in grades.values():
                    totalScore += int(grade)*subjectsAndCredits[everySubject]
                elif int(grade) not in grades.values():
                    print(
                        "That's kinda strange to know that you've been awarded such grade!")
                    countForStupid += 1
            except (KeyError, ValueError):
                print("You don't want to enter that, buddy! :)")
                countForStupid += 1
    choicesDict[everySubject]=grade

GPA = (totalScore/totalCredits)

os.system("cls")
if GPA == 0 or GPA == 10:
    print("\nYou're kinda the one that companies don't wanna recruit.")
    print("Anyway, here's your GPA: {}".format(GPA))
else:
    print(f"{name}, here is your score card:")
    for subject,val in choicesDict.items():
        print(f"{subject} : {val}")
    print(f"\nCGPA : {round(GPA,3)}")
    if countForFailure>0:
        print("Sorry to hear that you've failed %d subjects. Please do attempt supplementary exams ASAP."%(countForFailure))

input()