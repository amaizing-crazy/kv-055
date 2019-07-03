class Employee(object):
    def __init__(self,name, salary, experience, manager):
        self.name = name
        self.salary = salary
        self.experience = experience
        self.manager = manager

    def giveRaise(self, percent = 0.1, bonus = 0):
         print(101010)
         if self.experience > 5:
             bonus += 500
             percent += 0.2
         elif self.experience > 2:
             bonus += 200
             percent += 0
         return int(self.salary * (1 + percent) + bonus)

    def __str__(self):
         return '{0}, manager: {1} , experience:{2}'. format(self.name, self.manager, self.experience)
