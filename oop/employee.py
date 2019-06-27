class Employee(object):
    def __init__(self,name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience
    def giveRaise(self, percent, bonus):
         if self.experience > 5:
             bonus = 500
             percent = 0.2
         elif self.experience > 2:
             bonus = 200
         else:
             bonus =0
         self.salary = int(self.salary * (1 + percent) + bonus)
    def __str__(self):
         return '{0} : got salary: {1}'.format(self.name, self.salary)

class Manager(Employee):
    def __init__(self, name, salary, teamdev, teamdesi, highmanager,experience):
        Employee.__init__(self, name,salary,experience)
        self.teamdev = teamdev
        self.teamdesi = teamdesi
        self.highmanager= highmanager
    def giveRaise(self, percent, bonus):
        if (self.teamdev + self.teamdesi) > 10:
            bonus = 300
        elif(self.teamdev + self.teamdesi) > 5:
            bonus = 200
        elif  self.teamdev > (self.teamdev + self.teamdesi)/2:
            percent = 0.1
            bonus = 0
        else:
            bonus = 0
        Employee.giveRaise(self, percent, bonus)

class Dev(Employee):
    def __init__(self, name):
        self.name = name


class Designer(Employee):
    def __init__(self, effectiveness):
        self.effectiveness = effectiveness


john = Employee('John Sidorov', 100000, 10)
john.giveRaise(0.1,0)
print(john)
tom = Manager('Tom Jones', 100000, 10 ,5, 'BigBoss',10)
tom.giveRaise(0.1,0)
print(tom)


