class Student:
    def __init__(self,name,salaly):
        self.Name = name
        self.Salaly = salaly
    
    def Yearsalaly(self):
        return self.Salaly*12
    
Student1 = Student("tawan" ,12000)

print(Student1.Name , "เงินเดือน" , Student1.Yearsalaly() )