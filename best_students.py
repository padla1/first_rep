students = [
    {"name": "John", "surname": "Doe", "grades": [5, 5, 4, 4]},
    {"name": "Jane", "surname": "Doe", "grades": [4, 3, 4, 3, 5]},
    {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]},
    {"name": "Steve", "surname": "Jobs", "grades": [3, 5, 4, 3, 3, 5]},
    {"name": "Guido", "surname": "Van Rossum", "grades": [5, 3, 5, 4, 5, 5, 3, 5]},
    {"name": "Elon", "surname": "Musk", "grades": None}
]

def get_best_students (students):
    best_student = []
    best_average = 0
    for student in students:
        grades = student['grades']
        if student['grades'] is None:
            average_grade = 0
        else:
            average_grade = sum(grades)/len(grades)
        if average_grade>best_average:
            best_average = average_grade
            best_student=[student]
        elif average_grade == best_average:

            best_student.append(student)
    return best_student










print(get_best_students(students=students))