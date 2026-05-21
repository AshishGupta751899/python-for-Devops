# Calculate Class Attendance Percentage
# ○ Task: Write a program to calculate the percentage of classes attended by a
# student and determine their eligibility to sit in the exam.
# ○ Conditions:
# ■ Attendance percentage < 75%: Not eligible to sit in the exam.
# ■ Attendance percentage ≥ 75%: Eligible to sit in the exam.
# ○ Output: Display the attendance percentage and eligibility status.
total_classes = int(input("Enter the total number of classes: "))
classes_attended = int(input("Enter the number of classes attended: "))
attendance_percentage = (classes_attended / total_classes) * 100

print(f"Attendance Percentage: {attendance_percentage:.2f}%")
if attendance_percentage < 75:
    print("Not eligible to sit in the exam.")
else:
    print("Eligible to sit in the exam.")
    