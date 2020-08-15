# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def main():
    year_4_grades = []
    year_3_grades = []
    year_2_grades = []
    
    user_input = "derp"
    weighted_grade = 0
    total_divisible_grade = 0
    
    for i in range(3):
        gradeInfo = fourth_year_grading()
        weighted_grade += gradeInfo[0]
        total_divisible_grade += gradeInfo[1]
    for i in range(8):
        gradeInfo = third_year_grading()
        weighted_grade += gradeInfo[0]
        total_divisible_grade += gradeInfo[1]
    for i in range(8):
        gradeInfo = second_year_grading()
        weighted_grade += gradeInfo[0]
        total_divisible_grade += gradeInfo[1]
    print(weighted_grade)
    print(total_divisible_grade)
    print(weighted_grade/total_divisible_grade)
        
def convert_input_to_grade(user_input):
    basicGrade = 0
    if user_input.upper() == "A+":
        basicGrade = 9
    elif user_input.upper() == "A":
        basicGrade = 8
    elif user_input.upper() == "A-":
        basicGrade = 7
    elif user_input.upper() == "B+":
        basicGrade = 6
    elif user_input.upper() == "B":
        basicGrade = 5
    elif user_input.upper() == "B-":
        basicGrade = 4
    elif user_input.upper() == "C+":
        basicGrade = 3
    elif user_input.upper() == "C":
        basicGrade = 2
    elif user_input.upper() == "C-":
        basicGrade = 1
    elif user_input.toUpperCase() == "F":
        basicGrade = 0
    return basicGrade

def fourth_year_grading():
    gradeInfo = [0, 0]
    print("Enter a 4th year grade e.g. A ")
    grade = convert_input_to_grade(input())
    gradeInfo[0] = grade * 6 #60% of total grade
    gradeInfo[1] = 6 # what we'll divide by to get average
    return gradeInfo
    
def third_year_grading():
    gradeInfo = [0, 0]
    print("Enter a 3rd year grade e.g. A ")
    grade = convert_input_to_grade(input())
    gradeInfo[0] = grade * 3 # 30% of total grade
    gradeInfo[1] = 3 # what we'll divide by to get average
    return gradeInfo
    
def second_year_grading():
    gradeInfo = [0, 0]
    print("Enter a 2nd year grade e.g. A ")
    grade = convert_input_to_grade(input())
    gradeInfo[0] = grade * 1 # 10% of total grade
    gradeInfo[1] = 1 # what we'll divide by to get average
    return gradeInfo
    
main()