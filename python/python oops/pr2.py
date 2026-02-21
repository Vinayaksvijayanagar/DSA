class Employee:
    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        
    def apply_bonus(self):
        if self.salary >= 50000:
            self.salary = self.salary + ((10/100)*self.salary)
            print(self.salary)
        else:
            self.salary = self.salary + ((5/100)*self.salary)
            print(self.salary)
        return self.salary    
if __name__ == "__main__":
    s1 = Employee("vini",123,48000)
    s1.apply_bonus()