class Character:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def is_alife(self):
        return self.hp > 0

    def attack(self, enemy):
        enemy.hp -= self.dmg
        return f"{self.name} атакует {enemy.name} и наносит {self.dmg} урона"

    def get_status(self):
        return f"{self.name}: {self.hp} HP"


class Game:
    def __init__(self, user_name):
        self.player = Character(user_name, 100, 18)
        self.enemy = Character("Зомби", 80, 20)

    def player_turn(self):
        return self.player.attack(self.enemy)

    def enemy_turn(self):
        return self.enemy.attack(self.player)

    def is_over(self):
        return not (self.player.is_alife() and self.enemy.is_alife())

    def get_res(self):
        if self.player.is_alife():
            return "ты его замочил"
        else:
            return "он замочил тебя"

    def get_status(self):
        return f"{self.player.get_status()} | {self.enemy.get_status()}"




def info():
    name = input("введи свое имя воин: ")
    game = Game(name)

    print("⚔️битва начинается")
    while not game.is_over():
        input("\nКликни по Enter для атаки: ")
        print(game.player_turn())
        if game.enemy.is_alife():
            print(game.enemy_turn())
        print(game.get_status())
    print("\n💥 " + game.get_res())

if __name__ == "__main__":
    info()
