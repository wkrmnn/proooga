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

while True:
    project_id = input("Введите id проекта или СТОП для завершения: ")
    if project_id == "СТОП":
        break

    found = False
    for student in students:
        if student.id == project_id:
            print(f"Проект № {project_id} делал: {student.fio} он(а) получил(а) оценку - {student.score}")
            found = True
            break
    if not found:
        print("Ничего не найдено")
