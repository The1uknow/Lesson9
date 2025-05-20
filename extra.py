class Student:
    def __init__(self, name = "Иван", grnum = "10А", age = 18):
        self.name = name
        self.grnum = grnum
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def getgrnum(self):
        return self.grnum

    def setname(self, edit_name):
        self.setname = edit_name

    def setgrnum(self, edit_grnum):
        self.setgrnum = edit_grnum

students = [
    Student("Владимир", "10В", 17),
    Student("Далер", "10Л", 17),
    Student("Георгий", "10К", 18),
    Student("Самир", "10М", 18),
    Student("Лорес", "10Н", 19)
]

while True:
    print("список студентов: ")
    for i, student in enumerate(students, start = 1):
        print(f"{i}. {student.getname()}")
    try:
        w = int(input("\nвыбери номер студента (1-5 или 0 для чтобы выйти): ")) - 1
        if w == -1:
            break
        choice = students[w]

        while True:
            q = input("выберите действие:\nУзнать имя | Узнать возраст | Узнать группу | Изменить имя | Изменить группу | Назад: ").lower()

            if q == "узнать имя":
                print(choice.getname())
            elif q == "узнать возраст":
                print(choice.getage())
            elif q == "узнать группу":
                print(choice.getgrnum())
            elif q == "изменить имя":
                newname = input("введите новое имя: ")
                choice.setname(newname)
                print(f"имя успешно изменено на: {newname}")
            elif q == "изменить группу":
                newgroup = input("введите новую группу: ")
                choice.setgrnum(newgroup)
                print(f"группа успешно изменена на: {newgroup}")
            elif q == "Назад":
                break
            else:
                print("введи корректно")

    except (ValueError, IndexError):
        print("введи корректный номер студента пжалста: ")