# ACPC201 - Week 4 Labwork
# Rafi Miazi - K250249
# Designing a function for each grade and writing the results to a file.

import time


def is_HD(score) -> bool:
    return score >= 85


def is_D(score) -> bool:
    return score >= 75 and score < 85


def is_C(score) -> bool:
    return score >= 65 and score < 75


def is_P(score) -> bool:
    return score >= 50 and score < 65


def is_Fail(score) -> bool:
    return score < 50


def calculate_grade(score) -> str:
    if is_HD(score):
        return "HD"
    elif is_D(score):
        return "D"
    elif is_C(score):
        return "C"
    elif is_P(score):
        return "P"
    elif is_Fail(score):
        return "Fail"


def write_grades_to_file(scores, filename):
    try:
        with open(filename, 'w') as file:
            for score in scores:
                if score < 0 or score > 100:
                    file.write(f"Invalid score: {score}. Score must be between 0 and 100.\n")
                else:
                    grade = calculate_grade(score)
                    file.write(f"Score: {score}, Grade: {grade}\n")
    except IOError:
        print(f"Error occurred while writing to file: {filename}")


def main():
    start_time = time.time()

    scores = [90, 80, 70, 1055, 60, 40, 85, 75, 65, 55, 45, -5]
    filename = 'week04/grades.txt'
    write_grades_to_file(scores, filename)
    print(f"Grades written to {filename}")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nExecution Time: {execution_time} seconds")


if __name__ == "__main__":
    main()