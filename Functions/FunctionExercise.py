def calculate_grade(name, homework_score, assessment_score, final_score):
    total_score = homework_score + assessment_score + final_score
    percentage = (total_score/175)*100
    #175 comes from the total possbile score from each aargument (25+50+100 = 175)

    return name, percentage

# Take Inputs and assign to variables

name = str(input("Enter student's name: "))
homework = int(input("Enter homework score (/25): "))
assessment = int(input("Enter assessment score (/50): "))
final_exam = int(input("Enter final exam score (/100): "))

#Assign name and percentage to variables using function
student_name, grade_percentage = calculate_grade(name, homework, assessment, final_exam)

print(f"Student Name: {student_name}")
print(f"Grade Percentage: {grade_percentage}%")

