class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def showDetails(self):
        print(self.role)
        print(self.department)
        print(self.salary)
        
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","Development",60000)

s1 = Engineer("Alice",30)
s1.showDetails()