import random

class Student:
    def __init__(self, ชื่อเต็ม, ชื่อเล่น):
        self.name = ชื่อเต็ม
        self.nickname = ชื่อเล่น
        self.score = random.randint(0, 10)  # สุ่มคะแนนระหว่าง 0 ถึง 10
        self.score1 = random.randint(0, 10)  # สุ่มคะแนนระหว่าง 0 ถึง 10

    def Value(self):
        if self.score >= 5:
            print(f"ชื่อ-นามสกุล: {self.name}  ชื่อเล่น: {self.nickname}  (คะแนน: {self.score}): คุณสอบผ่าน")
        else:
            print(f"{self.name}   {self.nickname}  (คะแนน: {self.score}): คุณสอบตก")
            if self.score1 < 5:
                print(f"สอบเเก้ {self.score1} ไม่ผ่าน")
            else:
                print(f"สอบเเก้ {self.score1} ผ่าน")
        

# สร้างอินสแตนซ์ของ Student พร้อมคะแนนสุ่ม
Student1 = Student("นาย หนึ่งตะวัน แสงสูงเนิน", "กล้า")
Student2 = Student("นาย ชิติภัทร โสขะรัตน์", "ไนท์")
Student3 = Student("นางสาว เสาวลักษณ์ ปานแก้ว", "แตงกวาดอง")
Student4 = Student("นางสาว เตชิน ศรีพุฆ", "ไปร์ท")
Student5 = Student("นางสาว ปิติพงค์ ภูมิพงศ์","ปอน")

# เรียกฟังก์ชัน Value เพื่อแสดงผล
Student1.Value()
Student2.Value()
Student3.Value()
Student4.Value()
Student5.Value()
