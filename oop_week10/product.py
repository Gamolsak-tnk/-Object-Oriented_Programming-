class Product:
    def __init__(self, name, price, stock):
        self.name = name  
        self.price = price  
        self.__stock = stock        
    #เพิ่ม
    def add_stock(self, amount):
        if amount > 0:
            self.__stock += amount
            print(f"- เพิ่มสินค้า {self.name} จำนวน {amount} ชิ้นสำเร็จ ยอดคงเหลือในสต๊อก: {self.__stock} ชิ้น")
        else:
            print("จำนวนสินค้าที่เพิ่มต้องมากกว่า 0")
    #ลด
    def remove_stock(self, amount):
        if amount > 0 and amount <= self.__stock:
            self.__stock -= amount
            print(f"- ลดสินค้า {self.name} จำนวน {amount} ชิ้นสำเร็จ ยอดคงเหลือในสต๊อก: {self.__stock} ชิ้น")
        elif amount > self.__stock:
            print("จำนวนสินค้าในสต๊อกไม่เพียงพอ")
        else:
            print("จำนวนสินค้าที่ลดต้องมากกว่า 0")
    #เเก้ไขราคา
    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price
            print(f"- ปรับราคา {self.name} เป็น {self.price} บาทสำเร็จ")
        else:
            print("ราคาต้องมากกว่า 0 บาท")
    #ตรวจสอบ
    def check_product_info(self):
        print(f"ข้อมูลสินค้า:\n ชื่อสินค้า: {self.name}\n ราคา: {self.price} บาท\n สินค้าในสต๊อก: {self.__stock} ชิ้น")
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.__stock
        }
#เพิ่มสินค้า ชื่อ ไม้เเบดมินตัน VS Titan9 ราคา 1490 ในสต๊อกมี 30
product1 = Product("ไม้เเบดมินตัน VS titan9", 1490, 30)
#เพิ่ม
product1.add_stock(30)
#ลด
product1.remove_stock(30)
#เเก้ไขราคาไม้เเบด
product1.update_price(1390)
#ตรวจสอบ
product1.check_product_info()