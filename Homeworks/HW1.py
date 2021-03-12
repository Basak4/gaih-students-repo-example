#HMW1

lastNum = int(input("Please enter the final number "))
allNums = list(range(lastNum))
oddNums = [i for i in allNums if i % 2 != 0]
evenNums = [i for i in allNums if i % 2 == 0]
print("Odd numbers until ", lastNum, " :", oddNums)
print("Even numbers until ", lastNum, " :", evenNums)
oddNums.extend(evenNums)
print("Merge odd numbers and even numbers :", oddNums)
# oddNums.sort()  # to make more understandable
finalResult = [num1 * 2 for num1 in oddNums]
print("Multiply all values by 2 :", finalResult)

