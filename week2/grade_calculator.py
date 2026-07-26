# %%

# %%
def calculate_grade(score):
    if 85 <= score <= 100:
        return "High Distinction (HD)"
    elif 75 <= score < 85:
        return "Distinction (D)"
    elif 65 <= score < 75:
        return "Credit (C)"
    elif 50 <= score < 65:
        return "Pass (P)"
    elif 0 <= score < 50:
        return "Fail (F)"
    else:
        return "Invalid score. Please enter a score between 0 and 100."

# %%
score = float(input("Enter your score (0-100): "))
grade = calculate_grade(score)
print(f"you entered: {score}")
print(f"Your grade is: {grade}")


