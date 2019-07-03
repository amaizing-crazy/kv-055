from department import Department as D
from manager import Manager
from emp import Employee
from devdesigner import Developer, Designer
from myError import SalaryGivingError
from myError import WrongEmployeeRoleError


tom1 = Manager('Tom Jones', 100000, 10, None)
tom2 = Manager('Tom Sellek', 150000, 20, None)
angelina = Manager('Angelina Jolie', 150000, 20, None)
deptom1 = D('Office', 100000, 10, None)

#Adding Managers
deptom1.add_manager(tom1)
deptom1.add_manager(tom2)
deptom1.add_manager(angelina)
#Adding guys
john = Designer('John Sno', 100000, 1, 'Tom Jones', 0.99)
jack = Developer('Jack Black', 100000, 2, 'Tom Jones')
joe = Developer('Joe Moe', 100000, 5, 'Tom Sellek')
jane = Developer('Jane Cane', 100000, 10, 'Tom Sellek')

#deptom1.add_Team(john)
# print(deptom1.team_of_managers[0].name)
print('Managers:')
deptom1.show_Team_M()

#print(john)
try:
    tom1.add_Team(john)
    tom1.add_Team(jack)
    tom2.add_Team(joe)
    tom1.add_Team(jane)
    tom2.add_Team(angelina)
except WrongEmployeeRoleError as err:
    print("manager {0} has bad team".format(err.member))
print('Teams:')

tom1.show_Team()
tom2.show_Team()
print('Given raise:')
tom1.giveRaise(0.1,0)
# tom2.giveRaise(0.1,0)
#john.giveRaise(0.1)
# jane.giveRaise(0.1,0)
# joe.giveRaise(0.1,0)
# jack.giveRaise(0.1)
try:
    tom1.pay_Team()
    tom2.pay_Team()
    angelina.pay_Team()
except SalaryGivingError as sal:
    print('Error!!! Employee {0} has unexpected role!'. format(sal.member))
