# class Comment:
#     def __init__(self, username, text, likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
# a = input("Your name: ")
# person = Comment(a ,input("Write smth: "))


# class BankAccount:
#     def __init__(self, name, balance = 0):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, edit_deposit):
#         self.balance += edit_deposit
#
#     def cash(self, gain):
#         self.balance -= gain
#
#     def my_balance(self):
#         print(self.balance)


class User:
    def __init__(self, name, post, age, phone_num):
        self.name = name
        self.post = post
        self.age = age
        self.phone_num = phone_num

    def change_username(self, edit_username):
        self.change_username = edit_username

    def ch_num(self, edit_num):
        self.ch_num = edit_num

    def ch_p(self, edit_p):
        self.ch_p = edit_p














