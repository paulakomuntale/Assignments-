class Employee:
    def __init__(self):
        self.name = 'Paul'
        
emp=Employee()
print(emp.name)
        
#protected salary
class Employee:
    def __init__(self):
        self._salary = 50000

emp=Employee()
  #print(emp._salary)