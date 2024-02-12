class Studentik():
    fio = ''
    score = 0
    clas = ''
    id = 0

students = []
f = open('students.csv')
for i in range(10):
    students.append(Studentik())
    s = f.readline().split(',')
    students[i].fio = s[1]
    students[i].id = s[0]
    students[i].score = s[4]
    students[i].clas = s[3]

for i in range(1, len(students)):
    k = students[i]
    j = i - 1
    while j >= 0 and students[j].score < k.score:
        students[j + 1] = students[j]
        j -= 1
    students[j + 1] = k

for i in range(3):
    print(f"{i+1} место: {students[i].fio}")
