num = int(input("กรุณากรอกค่าเริ่มต้น : "))
num1 = int(input("กรุณากรอกค่าสุดท้าย : "))
for i in range (num,num1+1,1):
    if i %2 != 0:
        print(f"{i}")
    