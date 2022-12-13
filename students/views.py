from django.shortcuts import render

from .models import Student, Teacher
from datetime import datetime

# Create your views here.
def index(request):
    dt = datetime.now()
    dow = dt.weekday()
    teachers = Teacher.objects.filter(day=dow)
    students = Student.objects.filter(day=dow)

    coverage = []
    covered_students = []
    used_teacher_and_time = []
    for teacher in teachers:
        for slice in teacher.minutes_slices():
            for student in students:
                if student.time == slice and student.name not in covered_students:
                    coverage.append({'teacher': teacher.name, 'time': slice, 'student': student.name}) 
                    covered_students.append(student.name)
                    used_teacher_and_time.append({'teacher': teacher.name, 'time': slice})
                    break
            element = {'teacher': teacher.name, 'time': slice}
            if element not in used_teacher_and_time:
                coverage.append({'teacher': teacher.name, 'time': slice})
        coverage.append("/n")

    uncovered_students = [] 
    for student in students:
        if student.name not in covered_students:
            uncovered_students.append({"name": student.name, "time": student.time})

    return render(request, "students/index.html", {
        "datetime": dt,
        "today": dt.strftime('%A'),
        "coverage": coverage,
        "uncovered_students": uncovered_students, 
        "days": Teacher.objects.order_by().values('day').distinct()
    })


def day(request, day):
    teachers = Teacher.objects.filter(day=day)
    students = Student.objects.filter(day=day)

    coverage = []
    covered_students = []
    used_teacher_and_time = []
    for teacher in teachers:
        for slice in teacher.minutes_slices():
            for student in students:
                if student.time == slice and student.name not in covered_students:
                    coverage.append({'teacher': teacher.name, 'time': slice, 'student': student.name}) 
                    covered_students.append(student.name)
                    used_teacher_and_time.append({'teacher': teacher.name, 'time': slice})
                    break
            element = {'teacher': teacher.name, 'time': slice}
            if element not in used_teacher_and_time:
                coverage.append({'teacher': teacher.name, 'time': slice})
        coverage.append("/n")

    uncovered_students = [] 
    for student in students:
        if student.name not in covered_students:
            uncovered_students.append({"name": student.name, "time": student.time})

    return render(request, "students/day.html", {
        "day": day,
        "coverage": coverage,
        "uncovered_students": uncovered_students
    })


def result(request):
    dt = datetime.now()
    dow = dt.weekday()
    teachers = Teacher.objects.filter(day=dow)
    students = Student.objects.filter(day=dow)

    coverage = []
    covered_students = []
    for teacher in teachers:
        for slice in teacher.minutes_slices():
            for student in students:
                if student.time == slice and student.name not in covered_students:
                    coverage.append({'teacher': teacher.name, 'time': slice, 'student': student.name}) 
                    covered_students.append(student.name)
                    break
        coverage.append("/n")
    return render(request, "students/result.html", {

        "coverage": coverage
    })