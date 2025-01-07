class Student:
    def __init__(self, name, student_id, age):
        self.Name = name
        self.ID = student_id
        self.Age = age
        self.scores = {}  
        self.grades = {}  

    def input_scores(self):
        self.scores["คณิต"] = int(input('ใส่คะแนนคณิต: '))
        self.scores["ไทย"] = int(input('ใส่คะแนนภาษาไทย: '))
        self.scores["อังกฤษ"] = int(input('ใส่คะแนนอังกฤษ: '))
        self.scores["วิทย์"] = int(input('ใส่คะแนนวิทย์: '))
        self.scores["สังคม"] = int(input('ใส่คะแนนสังคม: '))
    
    def grades1(self, score):
        if score >= 80:
            grade = 4
        elif score >= 70:
            grade = 3
        elif score >= 60:
            grade = 2
        elif score >= 50:
            grade = 1
        else:
            grade = 0
        return grade  

    def calculate_grades(self):
        self.grades["คณิต"] = self.grades1(self.scores["คณิต"])
        self.grades["ไทย"] = self.grades1(self.scores["ไทย"])
        self.grades["อังกฤษ"] = self.grades1(self.scores["อังกฤษ"])
        self.grades["วิทย์"] = self.grades1(self.scores["วิทย์"])
        self.grades["สังคม"] = self.grades1(self.scores["สังคม"])
        return self.grades
    
    def grade_Average(self):
       
        total_points = self.grades["คณิต"] + self.grades["ไทย"] + self.grades["อังกฤษ"] + self.grades["วิทย์"] + self.grades["สังคม"]
        gpa = total_points / 5 
        return gpa  

student1 = Student("นาย สมชาย",1, 15) 
student2 = Student("นางสาว สมหญิง", 4, 16)  

print("\nข้อมูลนักเรียน:", student1.Name)
student1.input_scores()
print("ข้อมูลนักเรียน:", "ชื่อ:",student1.Name ,"หมายเลขประจำตัว:", student1.ID ,"อายุ:",student1.Age)
print("คะแนนเต่ล่ะวิชา:",student1.scores)
print("เกรดเเต่ล่ะวิชา:", student1.calculate_grades())
print("เกรดเฉลี่ย (GPA):", student1.grade_Average())

print("\nข้อมูลนักเรียน:", student2.Name)
student2.input_scores()
print("ข้อมูลนักเรียน:", "ชื่อ:",student2.Name ,"หมายเลขประจำตัว:", student2.ID ,"อายุ:",student2.Age)
print("คะแนนเเต่ล่ะวิชา:", student2.scores)
print("เกรดเเต่ล่ะวิชา:", student2.calculate_grades())
print("เกรดเฉลี่ย (GPA):", student1.grade_Average())