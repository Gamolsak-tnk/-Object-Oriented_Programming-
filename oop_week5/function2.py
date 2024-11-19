def mydog(a,b,c):
   if a > 0:
      b += a 
      print(f"ผลบวกรวม = {b}")     
      return b
   else:
      c += a
      print(f"ผลลบรวม = {c}") 
      return c
b = 0
c = 0
while True:
   a = int(input('ใส่ค่า : '))
   if a > 0:
      b = mydog(a,b,c)
   elif a < 0:
      c = mydog(a,b,c)
   else:
      break
   print(f'ผลบวกรวม = {b} ผลลบรวม = {c}')