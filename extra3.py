class Car:
    def __init__(self, color = "black", type = "sedan", year = 2077):
        self.color = color
        self.type = type
        self.year = year

    def begin(self):
        return "авто заведен"

    def out(self):
        return "авто заглушен"

    def yearmade(self):
        return f"год выпуска: {self.year}"

    def cartype(self):
        return f"тип авто: {self.type}"

    def carcolor(self):
        return f"цвет авто: {self.color}"

q = Car()

while True:
    adm = int(input("\nchoose act: 1)start | 2)stop | 3)year | 4)type | 5)color | 6)exit\n"))
    if adm == 1:
        print(q.begin())
    elif adm == 2:
        print(q.out())
    elif adm == 3:
        print(q.yearmade())
    elif adm == 4:
        print(q.cartype())
    elif adm == 5:
        print(q.carcolor())
    elif adm == 6:
        break
    else:
        print("введите корректно")