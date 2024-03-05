class Studentik():
    fio = ''
    score = 0
    clas = ''
    id = 0

students = []
f = open('students.csv')
for i in range(501):
    students.append(Studentik())
    s = f.readline().split(',')
    students[i].fio = s[1]
    students[i].id = s[0]
    students[i].score = s[4]
    students[i].clas = s[3]

for i in range(1, len(students)):
    k = students[i]
    j = i - 1
    while j >= 0 and students[j].score > k.score:
        students[j + 1] = students[j]
        j -= 1
    students[j + 1] = k

winners = []
count = 0
for student in students:
    if student.clas == '10':
        winners.append(student)
        count +=1
    if count == 3:
        break
print('10 класс')
for i in range(len(winners)):
    print('1 место:', winners[0].fio)
    print('2 место:', winners[1].fio)
    print('3 место:', winners[2].fio)