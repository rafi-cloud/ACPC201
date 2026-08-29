import time
import random

def main():
    startTime = time.time()

    student = {}

    student["ID"] = f"K{random.randint(200000,299999)}" # storing dynamically generated formatted string
    student["firstName"] = "Rafi"  # Storing normal string value
    student["lastName"] = "Miazi"
    student["gender"] = "Male"
    student["age"] = 23         # Storing Int type value
    student["isCurrentStudent"] = True  # storing boolean
    student["age"] = 24    # Updating the value of an existing key

    for key, value in student.items():  #running a for loop and retriving keys and values
        print(f"{key} : {value}")  # alternate: print(f"{key} : {student[key]}")

    endTime = time.time()
    print(f"\nExecution time is {endTime - startTime} seconds") #calculating execution time

if __name__ == "__main__":
    main()