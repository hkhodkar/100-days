student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student_name in student_scores:
    if student_scores[student_name] >= 91:
        student_grades[student_name] = "Outstanding"
    elif 81<= student_scores[student_name] <= 90:
        student_grades[student_name] = "Exceeds Expectations"
    elif 70< student_scores[student_name] <= 80:
        student_grades[student_name] = "Acceptable"
    else:
        student_grades[student_name] = "Fail"
        
print(student_grades);