from django.shortcuts import render

from .models import Student, Teacher
from datetime import datetime

# Create your views here.
def index(request):
    dt = datetime.now()
    dow = dt.weekday()
    teachers = Teacher.objects.filter(day=dow)
    students = Student.objects.filter(day=dow)

    # coverage = []
    # uncovered_students = list(students)
    # for teacher in teachers:
    #     covered_students = []
    #     for student in uncovered_students:
    #         if student.time == teacher.time:
    #             covered_students.append(student)
    #     coverage.append({'teacher': teacher, 'students': covered_students[:]})
    #     uncovered_students = [student for student in uncovered_students if student not in covered_students]  
    
    coverage = []
    covered_students = []
    for teacher in teachers:
        for slice in teacher.minutes_slices():
            for student in students:
                if student.time == slice and student.name not in covered_students:
                    coverage.append({'teacher': teacher.name, 'time': slice, 'student': student.name}) 
                    covered_students.append(student.name) 
                if [{'teacher': teacher.name, 'time': slice}] not in coverage:
                    coverage.append({'teacher': teacher.name, 'time': slice})



    unique_values = []
    for x in coverage:
        if x not in unique_values:
            unique_values.append(x)

    uncovered_students = [] 
    for student in students:
        if student.name not in covered_students:
            uncovered_students.append(student.name)

    return render(request, "students/index.html", {
        "datetime": dt,
        "today": dt.strftime('%A'),
        "coverage": unique_values,
        "uncovered_students": uncovered_students
    })