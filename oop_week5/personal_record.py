s = ()
Value = int(input("จำนวนคนที่จะป้อน : "))
studen = {'name':s,'nickname':s,'id':s,'hopby':s,'colors':s}
for i in range(Value):
    print("ข้อมูคนที่ : ",(i+1))
    s = input('กรุณากรอกชื่อ:')
    studen['name'] = s
    s = input('กรุณากรอกชื่อกรุณากรอกชื่อเล่น :')
    studen['nickname'] = s
    s = int(input('กรุณากรอกรหัสประจำตัวนักศึกษา :'))
    studen['id'] = s
    s = input('กรุณากรอกงานอดิเรก :')
    studen['hopby'] = s
    s = input('กรุณากรอกสีที่ชอบ :')
    studen['colors'] = s
    print(studen)