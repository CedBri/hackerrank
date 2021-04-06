from collections import namedtuple

N, students = int(input()), namedtuple('students', input().split())
stud = [students(*input().split()) for _ in range(N)]
print(sum(float(i.MARKS) for i in stud) / N)
