name = input("กรุณากรอกชื่อ : ")
age = input("กรุณากรอกอายุ : ")
id = input("กรุณากรอกรหัสประจำตัว : ")
year = input("กรุณากรอกชั้นปี : ")
nickname = input("กรุณากรอกชื่อเล่น : ")

h = int(input("กรุณากรอกส่วนสูง : "))
w = int(input("กรุณากรอกน้ำหนัก : "))
total = h + w

print("ชื่อ: " + name + " อายุ: " + age)
print("รหัสประจำตัว: " + id + " ระดับชั้นปี: " + year)
print("ชื่อเล่น: " + nickname)
print("ส่วนสูง: " + str(h) + " น้ำหนัก: " + str(w))
print("ส่วนสูง + น้ำหนัก = " + str(total))
