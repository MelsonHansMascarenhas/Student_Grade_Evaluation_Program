try:
    marks = float(input("Enter the student's marks (0-100): "))
    if marks < 0 or marks > 100:
        print("Invalid marks. Please enter a value between 0 and 100.")
    else:
        if marks >= 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print(f"The grade is: {grade}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
