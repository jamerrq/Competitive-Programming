import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


class Student(object):

    def __init__(self, student_id):
        self.student_id = student_id
        self.religion = None
        self.mates = []

    def spread_the_religion(self, religion):
        self.religion = religion
        for mate in self.mates:
            if mate.religion is None:
                mate.spread_the_religion(religion)


case = 0
while True:

    n, m = readList()
    students = [Student(i) for i in range(n)]

    if n + m:
        for _ in range(m):
            i, j = readList()
            students[i - 1].mates.append(students[j - 1])
            students[j - 1].mates.append(students[i - 1])

        for i in range(n):
            if students[i].religion is not None:
                continue
            students[i].spread_the_religion(i)

        religions = set()
        for student in students:
            religions.add(student.religion)

        print(f'Case {case + 1}: {len(religions)}')
        case += 1

    else:
        break
