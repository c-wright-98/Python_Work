def calculate_grade(name, homework_score, assessment_score, final_score):
    total_score = homework_score + assessment_score + final_score
    percentage = (total_score/175)*100
    #175 comes from the total possbile score from each aargument (25+50+100 = 175)
    