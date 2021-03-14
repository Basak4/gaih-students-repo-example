#HMW3

#  i know that i can make it shorter with just one loop, this is not a useful way..

maxSt = 0
name = (input("Please enter your name: "))
surname = (input("Please enter your surname: "))
midtermGrade = float(input("Please enter your midterm grade: "))
projectGrade = float(input("Please enter your project grade: "))
finalGrade = float(input("Please enter your final grade: "))
passingGrade = (float(midtermGrade)*0.3) + (float(projectGrade)*0.3) + (float(finalGrade)*0.4)
print("Your passing grade is :", passingGrade)
print("-------------------------------")

name2 = (input("Please enter your name: "))
surname2 = (input("Please enter your surname: "))
midtermGrade2 = float(input("Please enter your midterm grade: "))
projectGrade2 = float(input("Please enter your project grade: "))
finalGrade2 = float(input("Please enter your final grade: "))
passingGrade2 = (float(midtermGrade2)*0.3) + (float(projectGrade2)*0.3) + (float(finalGrade2)*0.4)
print("Your passing grade is :", passingGrade2)
print("-------------------------------")

name3 = (input("Please enter your name: "))
surname3 = (input("Please enter your surname: "))
midtermGrade3 = float(input("Please enter your midterm grade: "))
projectGrade3 = float(input("Please enter your project grade: "))
finalGrade3 = float(input("Please enter your final grade: "))
passingGrade3 = (float(midtermGrade3)*0.3) + (float(projectGrade3)*0.3) + (float(finalGrade3)*0.4)
print("Your passing grade is :", passingGrade3)
print("-------------------------------")

name4 = (input("Please enter your name: "))
surname4 = (input("Please enter your surname: "))
midtermGrade4 = float(input("Please enter your midterm grade: "))
projectGrade4 = float(input("Please enter your project grade: "))
finalGrade4 = float(input("Please enter your final grade: "))
passingGrade4 = (float(midtermGrade4)*0.3) + (float(projectGrade4)*0.3) + (float(finalGrade4)*0.4)
print("Your passing grade is :", passingGrade4)
print("-------------------------------")

name5 = (input("Please enter your name: "))
surname5 = (input("Please enter your surname: "))
midtermGrade5 = float(input("Please enter your midterm grade: "))
projectGrade5 = float(input("Please enter your project grade: "))
finalGrade5 = float(input("Please enter your final grade: "))
passingGrade5 = (float(midtermGrade5)*0.3) + (float(projectGrade5)*0.3) + (float(finalGrade5)*0.4)
print("Your passing grade is :", passingGrade5)
print("-------------------------------")

average = (passingGrade + passingGrade2 + passingGrade3 + passingGrade4 + passingGrade5) / 5
print(average)
if passingGrade > maxSt:
    maxSt = passingGrade
elif passingGrade2 > maxSt:
    maxSt = passingGrade2
elif passingGrade3 > maxSt:
    maxSt = passingGrade3
elif passingGrade4 > maxSt:
    maxSt = passingGrade4
elif passingGrade5 > maxSt:
    maxSt = passingGrade5
print("Highest grade is : ", maxSt)






'''
#  like this
average = 0
count = 0
while count < 5:
    print("Student", count + 1)
    name = (input("Please enter your name: "))
    surname = (input("Please enter your surname: "))
    midtermGrade = float(input("Please enter your midterm grade: "))
    projectGrade = float(input("Please enter your project grade: "))
    finalGrade = float(input("Please enter your final grade: "))
    passingGrade = (float(midtermGrade)*0.3) + (float(projectGrade)*0.3) + (float(finalGrade)*0.4)
    print("Your passing grade is :", passingGrade)
    print("--------------------------------")
    average = average+passingGrade
    tempGrade = passingGrade
    count = count + 1

    for i in range(0, 5):
        if tempGrade > (average/5):
            print("You passed")
            print("--------------------------------")
'''


