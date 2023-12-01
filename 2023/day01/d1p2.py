# --- Part Two ---

# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

def checkForwards(list, line):
    firstNum = -1

    for i in range(len(line)):
        for key in list:
            if i <= (len(line) - len(key)):
                searchResult = line.find(key, i, i + len(key))
                if searchResult != -1:
                    firstNum = list[key]
                    return firstNum

def checkBackwards(listReversed, line):
    lastNum = -1
    for i in range(len(line)):
        for key in listReversed:
            if i <= (len(line)-len(key)):
                reversedLine=''.join(reversed(line))
                searchResult = reversedLine.find(key,i,(i+len(key)))
                if searchResult != -1:
                    lastNum = listReversed[key]
                    return lastNum

list = {'one': 1,'two': 2,'three': 3,'four' : 4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
listReversed = {'eno':1,'owt':2,'eerht':3,'ruof':4,'evif':5,'xis':6,'neves':7,'thgie':8,'enin':9,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
runTotal = 0
with open("input.txt", "r") as keytext:
    for line in keytext:
        firstNum = str(checkForwards(list, line))
        lastNum = str(checkBackwards(listReversed, line))
        if lastNum == -1 or lastNum == 'None':
            lineTotal = int(firstNum + firstNum)
            print(lineTotal)
            runTotal += lineTotal
        else:
            lineTotal = int(firstNum + lastNum)
            print(lineTotal)
            runTotal += lineTotal
        print(line)

print(runTotal)