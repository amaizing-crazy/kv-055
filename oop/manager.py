from emp import Employee
from devdesigner import Developer, Designer
from myError import SalaryGivingError
from myError import WrongEmployeeRoleError

class Manager(Employee):
    def __init__(self, name, salary, experience, manager):
        Employee.__init__(self, name,salary,experience, manager)
        self.team = []

    def pay_Team(self):
        if len(self.team)< 1:
            raise SalaryGivingError(self.name)
        for x in self.team:
            print('{0} had salary {1} after raise got salary: {2}'.format(x.name, x.salary, x.giveRaise()))

    def giveRaise(self, percent = 0.1 , bonus=0):
        print(999)
        while True:
            # try:
            if len(self.team)< 1:
                #raise SalaryGivingError(Manager.__name__)
                print(111)
            # except SalaryGivingError as err:
            #     print(err.message)
            # else:
            #print('Giving Raise: ')
            d = 0
            for i in range(len(self.team)):
                 if isinstance(i, Developer) == True:
                     d = d + 1
            if (len(self.team)) > 10:
                bonus = 300
            elif(len(self.team)) > 5:
                bonus = 200
            elif (d > len(self.team)/2):
                percent = 0.1
                bonus = 0
            else:
                bonus = 0
            return super(Manager, self).giveRaise(percent, bonus)

    def add_himanager(self, highmanager):
        self.highmanager= highmanager

    def add_Team(self, member):
        if isinstance(member, Manager) == True:
            raise WrongEmployeeRoleError('Exp','Message',member.name)
        self.team.append(member)

    def show_Team(self):
        for x in self.team:
            print(x)
