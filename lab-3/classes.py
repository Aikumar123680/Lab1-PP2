class Strings:
    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

s = Strings()
s.getString()
s.printString()


class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

length = int(input("Enter the len: "))
sq = Square(length)
print("Square of area totally: ", sq.area())


class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

length = int(input("Enter the len: "))
width = int(input("Enter the width: "))
rect = Rectangle(length, width)
print("Square of rectangle totally: ", rect.area())


import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, x1, y2):
        self.x = x1
        self.y = y2

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


x1 = int(input("Enter the x: "))
y1 = int(input("Enter the y: "))
x2 = int(input("Enter another point x: "))
y2 = int(input("Enter another point y: "))

point1 = Point(x1, y1)
point2 = Point(x2, y2)

point1.show()
point2.show()

print("Distance between points: ", point1.dist(point2))


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}$. New balance: {self.balance}$")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Available balance: {self.balance}$")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawn: {amount}$. New balance: {self.balance}$")
        else:
            print("Withdrawal amount must be positive.")


account = BankAccount(input("Enter your name: "), int(input("Your account balance is: ")))
account.deposit(int(input("How much money you want to deposit: ")))

account.withdraw(int(input("How much money you want to withdraw: ")))
print(f"Final balance: {account.balance}$")


def prime_numbers():
    numbers = input("Enter numbers: ").split()
    numbers = [int(num) for num in numbers]
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_nums = [num for num in numbers if is_prime(num)]
    print("Prime numbers:", prime_nums)

prime_numbers()
