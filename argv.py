import sys

# Class
class user():
    def __init__(self):
        self.name = input("Your name?")
        self.password = input("Enter your password")
    def print(self):
        print("Name: " + self.name)
        print("password: " + self.password)


class admin(user):
    def __init__(self):
        user.__init__(self)
        self.root = input("Enter root password")
    def print(self):
        print("Name: " + self.name)
        print("password: " + self.password)
        print("root: "+ self.root)

# Program
k = sys.argv
if k[1] == 'run':
    print("Server is runing")
elif k[1] == 'create':
    if k[2] == 'user':
        user1 = user()
        print("Info about you")
        user1.print()
    if k[2] == 'admin':
        admin1 = admin()
        print("Info about you")
        admin1.print()

