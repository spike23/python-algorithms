

def sorter(students):
    """

    :param students: nested list with names and marks
    :return: None
    """
    students.sort(key=lambda student: (student[1], student[0]))
    second = [student[1] for student in students if student[1] != students[0][1]][0]
    res = [student for student in students if student[1] == second]
    for mark in res:
        print(mark[0])


if __name__ == '__main__':
    """
    5
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39
    """
    # students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    sorter(students)
