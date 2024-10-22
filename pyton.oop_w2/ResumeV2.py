name = input("กรุณากรอกชื่อ : ")
age = input("กรุณากรอกอายุ : ")
id = input("กรุณากรอกรหัสประจำตัว : ")
year = input("กรุณากรอกชั้นปี : ")
nickname = input("กรุณากรอกชื่อเล่น : ")

h = int(input("กรุณากรอกส่วนสูง : "))
w = int(input("กรุณากรอกน้ำหนัก : "))
total = h + w

print(f"ชื่อ: {name} อายุ: {age}")
print(f"รหัสประจำตัว: {id} ระดับชั้นปี: {year}")
print(f"ชื่อเล่น:{nickname}")
print(f"ส่วนสูง: {h} น้ำหนัก:{w} ")
print(f"ส่วนสูง + น้ำหนัก {total} ")
