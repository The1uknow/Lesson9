class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def substraction(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

args = Math(10, 2)

print(f"сумма: {args.addition()}\nразница: {args.substraction()}\nпроизведение: {args.multiply()}\nчастное: {args.division()}")