print("โปรเเกรมตัดเเกรม")
score = int(input("กรอกคะเเเนน : "))
if score >= 80:
    print("เกรด 4")
elif score >= 70:
    print("ได้เกรด 3")
elif score >= 60:
    print("เกรด 2")
elif score >= 50:
    print("เกรด 1")
elif score == 5:
    print("เกรด 0")

else :
    print("คูณได้เกรด 0")
    print ("ต้องการเเก้ หรือไม่ ต้องการพิมพ์ 1 ไม่ต้องการพิมพ์ 2 ")
    c = int(input("กรอกตัวเลือก : "))
    if c == 1:
        print(f"คูณขาดคะเเนนอีก {50 - score}")
    elif c == 2:
        print("สอบตกเหมือนกัน")
    else:
        print("กรุณาเลือกเเค่ 1 กับ 2")