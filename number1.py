class Studentik():
    pass

j = 0
students = []
f = open('students.csv')
name = f.readline().strip()
for i in f:
    students.append(Studentik())
    s = i.strip().split(',')
    students[i].fio = s[1]
    students[i].id = s[0]
    students[j].title = s[2]
    students[i].score = s[4]
    students[i].clas = s[3]
    j+=1

for i in students:
    s = 0
    k = 0
    if i.score == 'None':
        for j in students:
            if j.clas == i.clas and j.score!='None':
                k+=1
                s+= int(j.score)
        i.score = f'{s/k:.3f}'
fil = open('students_new.csv', 'w')
print(name, file=fil)
for i in students:
    print(i.id,',',i.fio,',',i.title,',', i.clas,',', i.score,',',file = fil)

ff='Хадаров Владимир Валериевич'

for i in range(len(students)):
    if students[i].fio == ff:
        print('Ты получил:', students[i].score,', за проект -', students[i].id)
        break

fil.close()