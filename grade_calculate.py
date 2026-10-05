def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")

while True:
    try:
        marks = float(input("Enter marks (0-100): "))

        if marks >= 0 and marks <= 100:
            break
        else:
            print("Please enter marks between 0 and 100.")

    except ValueError:
        print("Please enter a valid number.")

grade = calculate_grade(marks)

print("\n🎓 Student Grade Result")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)

if grade == "A":
    print("Excellent work! 🌟")
elif grade == "B":
    print("Great job! 👍")
elif grade == "C":
    print("Good effort! Keep improving! 💪")
elif grade == "D":
    print("You passed. Keep working hard! 📚")
else:
    print("Don't give up. Keep practicing! 💪")
