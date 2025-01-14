class Animal:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f"ชื่อ {self.name} อายุ {self.age} ปี มีสี {self.color}"
class Dog(Animal):
    def __init__(self, name, age, color,race):
        super().__init__(name, age, color)
        self.race = race
    def showinfo(self):
        return f"หมาพันธ์ {self.race} มี {super().showinfo()}"

animal = Animal("ปีเตอร์",12,"ดำ")
dog1 = Dog("โน่",5,"ดำ","หลังอาน")

print(dog1.showinfo())
