# ACPC201 - Week 5 Labwork
# Rafi Miazi - K250249
# Given a list of numbers, calculate the sum of the numbers that are even.

import time

def makeList(start, end):
    lst = []
    for i in range(start, end+1):
        lst.append(i)
    return lst

def calculateSumOfEvenNum(itr) -> int:
    total = 0
    for item in itr:
        if item % 2 == 0:
            total += item
    return total

def main():
    startNum = int(input("please enter the starting number: "))
    endNum = int(input("Please enter the ending number: "))

    startTime = time.time()
    lst = makeList(startNum, endNum)
    total = calculateSumOfEvenNum(lst)
    endTime = time.time()

    print(f"The sum of all the even numbers from {startNum} to {endNum} is ==> {total}")
    print(f"Execution time is {endTime - startTime} seconds")

if __name__ == "__main__":
    main()