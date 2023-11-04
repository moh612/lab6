from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students_view(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'students.html', {'students': students, 'form': form})

def courses_view(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    return render(request, 'courses.html', {'courses': courses, 'form': form})

def details_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    available_courses = Course.objects.exclude(students=student)
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        if course_id:
            course = Course.objects.get(pk=course_id)
            student.courses.add(course)
            student.save()
    return render(request, 'details.html', {'student': student, 'available_courses': available_courses})


