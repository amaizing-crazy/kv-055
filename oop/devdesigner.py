from emp import Employee

class Developer(Employee):
    def __init__(self, name, salary, experience, manager):
        Employee.__init__(self, name, salary, experience, manager)


class Designer(Employee):
    def __init__(self, name, salary, experience, manager, effectiveness):
        Employee.__init__(self, name, salary, experience, manager)
        self.effectiveness = effectiveness

    def giveRaise(self, percent = 0.1, bonus = 0):
        print(888)
        return super(Designer, self).giveRaise(percent, bonus) * self.effectiveness
