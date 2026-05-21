#  Task: Students Interview Eligibility Checker
# ● Objective:you have to design a javascript script that checks whether a student is
# eligible for an interview based on their academic score attendance percentage
# and extracurricular participation.
# ● Input:
# ○ Academic Score (percentage): A floating-point number representing the
# student's academic score. Ex .78.88
# ○ Attendance Percentage: A floating-point number representing the
# student's attendance percentage. Ex.85.88
# ○ Extracurricular Participation: This indicates whether the student has
# participated in any extracurricular activities. Ex.Yes/no
# Conditions for Interview Eligibility:
# 1. The student’s academic score must be 60 or above.
# 2. The student’s attendance percentage must be 75 or above.
# 3. The student should have participated in at least one extracurricular activity.

academic_score = float(input("Enter the academic score (percentage): "))
attendance_percentage = float(input("Enter the attendance percentage: "))
extracurricular_participation = input("Have you participated in any extracurricular activities? (Yes/No): ").strip().lower()
if academic_score >= 60 and attendance_percentage >= 75 and extracurricular_participation == "yes":
    print("You are eligible for the interview.")
else:
    print("You are not eligible for the interview.")
