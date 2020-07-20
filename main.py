"""First, we got to get the credits in a dictionary"""
# Creating the dictionary for first semester with credits and subjects

totalCredits = 21

grades = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "F": 0}

subjectsAndCredits = {"COSM": 4, "Analog and Digital Electronics": 3, "Data Structures": 4,
                      "COA": 3, "C++": 2, "ADE-LAB": 1, "DS-LAB": 1.5, "IT-LAB": 1.5, "C++ LAB": 1}


totalScore = 0

name = input("Well, what's you're name, buddy?\n")


for everySubject in subjectsAndCredits:
    try:
        try:
            grade = input("What's your grade for {}: ".format(everySubject))
            check = eval(grade)
            if type(check) == int and check in grades.values():
                totalScore += check*subjectsAndCredits[everySubject]

        except NameError:
            if grade.upper() in grades.keys():
                totalScore += grades[grade.upper()] * \
                    subjectsAndCredits[everySubject]
    except SyntaxError:
        print("So, your GPA consists of whitespaces, mate?")
        break

GPA = (totalScore/totalCredits)

if GPA == 0 or GPA == 10:
    print("You're kinda the one that companies don't wanna recruit.")
    print("Anyway, here's your GPA: {}".format(GPA))
else:
    print("{}, here's your GPA : {}".format(name.title(), GPA))
