# UPSC Selection Process
# ○ Task: Simulate the UPSC selection process with the following steps:
# 1. Eligibility Check
# ■ Criteria:
# ■ Age: 21–32 years.
# ■ Graduate status: Must be a graduate.
# ■ Nationality: Must be "Indian".
# ■ Output:
# ■ If eligible, proceed to Prelims.
# ■ If ineligible, display the reason for ineligibility.
# 2. Prelims Exam
# ■ Processing: Check if the candidate’s score ≥ cut-off.
# ■ Output:
# ■ If passed, proceed to Mains.
# ■ If failed, display "You failed the Prelims."
# 3. Mains Exam
# ■ Processing: Check if the candidate’s score ≥ cut-off.
# ■ Output:
# ■ If passed, proceed to Interview.
# ■ If failed, display "You failed the Mains."
# 4. Interview
# ■ Processing: Check if the candidate’s score ≥ cut-off.
# ■ Output:
# ■ If passed, display "Congratulations! You have cleared the
# UPSC."
# ■ If failed, display "You failed the Interview."
# ○ Final Output: Use nested conditional statements to simulate the entire process.
# __________________________________________________________
age = int(input("Enter your age: "))
graduate_status = input("Are you a graduate? (yes/no): ").strip().lower()
nationality = input("Enter your nationality: ").strip().lower()
if 21 <= age <= 32 and graduate_status == "yes" and nationality == "indian":
    prelims_score = float(input("Enter your Prelims score: "))
    prelims_cutoff = 50.0
    if prelims_score >= prelims_cutoff:
        mains_score = float(input("Enter your Mains score: "))
        mains_cutoff = 60.0
        if mains_score >= mains_cutoff:
            interview_score = float(input("Enter your Interview score: "))
            interview_cutoff = 70.0
            if interview_score >= interview_cutoff:
                print("Congratulations! You have cleared the UPSC.")
            else:
                print("You failed the Interview.")
        else:
            print("You failed the Mains.")
    else:
        print("You failed the Prelims.")  

