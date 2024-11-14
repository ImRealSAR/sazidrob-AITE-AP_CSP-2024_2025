def grade_points(p):
    if p >= 90:
        return 4
    elif p >= 80:
        return 3
    elif p >= 70:
        return 2
    elif p >= 60:
        return 1
    else:
        return 0

courses = []
grades = []

def list_courses():
    n = int(input("Enter number of courses you're taking: "))
    for i in range(n):
        course_name = input("Enter course name: ")
        courses.append(course_name)

    for c in courses:
        points = input(f"Enter your final grade percentage for {c}: ")
        while not points.isdigit():
            print('Entry not valid')
            points = input(f"Enter your final grade percentage for {c}: ")
        while int(points) > 100:
            print('Entry not valid')
            points = input(f"Enter your final grade percentage for {c}: ")
        points = int(points)
        grades.append(grade_points(points))

def compute_my_gpa():
    total_points = sum(grades)
    gpa = total_points / len(grades)
    print(f"{gpa}")

list_courses()
compute_my_gpa()
