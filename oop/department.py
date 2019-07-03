from manager import Manager
from emp import Employee

class Department(Manager):
    def __init__(self,name,salary,experience,manager):
        Employee.__init__(self, name, salary, experience, manager)
        self.team_of_managers = []

    def add_manager(self, member):
        self.team_of_managers.append(member)

    def show_Team_M(self):
        for x in self.team_of_managers:
            print(x)

    def __str__(self):
         return '{0} : got salary: {1}'.format(self.name, self.salary)
