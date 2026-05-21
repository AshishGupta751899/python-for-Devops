# .Task : Student Grading System
# Create a javascript program to calculate a student's grade based on their marks.
# Task:
# 1. Input: Prompt the user to enter their marks.
# 2. Criteria:
# ○ Grade A: 90–100
# ○ Grade B: 80–89
# ○ Grade C: 70–79
# ○ Grade D: 60–69
# ○ Grade E: 50–59
# ○ Grade F: 0–49
# ○ Invalid marks: Outside the range 0–100.
# 3. Output: Display the grade or an error message for invalid marks.

marks = float(input("Enter your marks: "))
if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
elif 60 <= marks < 70:
    print("Grade D")
elif 50 <= marks < 60:
    print("Grade E")
elif 0 <= marks < 50:
    print("Grade F")
else:
    print("Invalid marks. Please enter a value between 0 and 100.")
    