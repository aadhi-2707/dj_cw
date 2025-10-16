from django.shortcuts import render

def employee_directory(request):
    employees = [
        {'name': 'Adithyan', 'job_title': 'Software Engineer', 'salary': 60000, 'is_full_time': True},
        {'name': 'Manu', 'job_title': 'Designer', 'salary': 45000, 'is_full_time': False},
        {'name': 'Manya', 'job_title': 'HR Manager', 'salary': 55000, 'is_full_time': True},
    ]

    return render(request, 'employee_directory.html', {'employees': employees})
