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


print("Enter marks for 5 subjects (out of 100):")
subject1 = float(input("Subject 1: "))  
subject2 = float(input("Subject 2: "))  
subject3 = float(input("Subject 3: ")) 
subject4 = float(input("Subject 4: "))  
subject5 = float(input("Subject 5: "))  
total = subject1 + subject2 + subject3 + subject4 + subject5
average = total / 5
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 50:
    grade = 'D'
else:
    grade = 'Fail'
print("\n--- Result ---")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")