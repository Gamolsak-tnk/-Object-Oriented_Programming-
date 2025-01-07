class Em :
    def __init__(self,name,job,salary):
        self.Name = name
        self.Job = job
        self.Salary = salary
    
    def salary1(self):
        return self.Salary * 12 

em1 = Em("โซเฟีย","ครู",12000)
em2 = Em("ปีเตอร์","หมอ",45000)
em3 = Em("ป็อป","โปรเเกรมเมอร์",40000)

print(em1.Name, "ประกอบอาชีพ", em1.Job, "มีเงินเดือนทั้งปี", em1.salary1())
print(em2.Name, "ประกอบอาชีพ", em2.Job, "มีเงินเดือนทั้งปี", em2.salary1())
print(em3.Name, "ประกอบอาชีพ", em3.Job, "มีเงินเดือนทั้งปี", em3.salary1())


