class Unit:
    def __init__(self, power, speed, stamina):
        self.power = power
        self.speed = speed
        self.stamina = stamina

    def change_power(self, edit_power):
        self.power = edit_power

    # assasin = Unit(50, 100, 30)
    # tank = Unit(15, 20, 100)
    #
    # print(assasin.power)
    # print(assasin.stamina, tank.stamina)


#     def form(self):
#         print("Formation for attack...")
# assasin = Unit(50, 100, 30 )
# assasin.form()


tank = Unit(15, 20, 100)
tank.change_power(20)
print(tank.power)