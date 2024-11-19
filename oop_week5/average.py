num = []
num1 = int(input("กรุณาใส่จำนวนค่า : "))
for i in range(num1):
    s = int(input("กรุณาใส่ค่า : ")) 
    num.append(s)  
dee = (sum(num) // len(num))
print(dee)