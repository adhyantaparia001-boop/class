


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def get_annual_salary(self):
        return self.salary
class Manager(Employee):
    def __init__(self,bonus,name,salary):
        self.bonus = bonus
        super().__init__(name,salary)
    def get_annual_salary(self):
        salary_afterbonus = self.salary + self.bonus
        print(f'{salary_afterbonus} is the complete salary')
emp1 = Employee('AA',12345)
Manager1 = Manager(2500,'AAA',128900)
Manager1.get_annual_salary()
class Bankaccount :
    def __init__(self,__balance):
        self.balance = __balance
    def withdraw(self,amount):
        if amount > self.balance:
            print('Not enough balance')
        else:
            self.balance -= amount
    def deposit(self,amount):
        self.balance += amount
    @property
    def Get_Balance(self):
        return self.balance
myaccount = Bankaccount(10000000)
print(myaccount.Get_Balance)
myaccount.withdraw(200000)
myaccount.deposit(1000)
print(myaccount.Get_Balance)
class shape:
    def area(self):
        pass
class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
class Circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 22/7 * self.radius*self.radius
def calc_area(shape):
    print(shape.area())
a = Circle(11)
calc_area(a)