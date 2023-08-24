def grading_system(marks):
    avg_marks = sum(marks)/len(marks)
    min_marks = min(marks)
    max_marks = max(marks)
    grade_list = []
    for mark in marks:
        if mark >= avg_marks+10:
            grade_list.append('A')
        elif mark >= avg_marks+5:
            grade_list.append('B')
        elif mark >= avg_marks-5:
            grade_list.append('C')
        else:
            grade_list.append('D')
    grades = {}
    for i in range(len(marks)):
        grades['Student '+str(i+1)] = grade_list[i]
    return grades