# ACPC201 - Week 6 Labwork
# Rafi Miazi - K250249
# Split "Kent Institute Australia" into substrings and count each length.

import time
def splitIntoSubStrings(str) -> list:
    return str.split(" ")

def countLength(str) -> int:
    return len(str)

def main():
    startTime = time.time()

    text = "Kent Institute Australia"

    substringList= splitIntoSubStrings(text)
    print(f"\nOriginal string: {text}")
    print(f"Number of substrings found: {len(substringList)}\n")
    
    for substring in substringList:
        print(f"Substring: {substring}  length: {countLength(substring)}")

    endTime = time.time()

    print(f"\nExecution time is {endTime - startTime} seconds")

if __name__ == "__main__":
    main()