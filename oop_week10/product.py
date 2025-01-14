class Product:
    def __init__(self, name, price, stock):
        self.name = name  
        self.price = price  
        self.__stock = stock        

    # เพิ่ม
    def add_stock(self, amount):
        if amount > 0:
            self.__stock += amount
            print(f"- เพิ่มสินค้า {self.name} จำนวน {amount} ชิ้นสำเร็จ ยอดคงเหลือในสต๊อก: {self.__stock} ชิ้น")
        else:
            print("จำนวนสินค้าที่เพิ่มต้องมากกว่า 0")

    # ลด
    def remove_stock(self, amount):
        if amount > 0 and amount <= self.__stock:
            self.__stock -= amount
            print(f"- ลดสินค้า {self.name} จำนวน {amount} ชิ้นสำเร็จ ยอดคงเหลือในสต๊อก: {self.__stock} ชิ้น")
        elif amount > self.__stock:
            print("จำนวนสินค้าในสต๊อกไม่เพียงพอ")
        else:
            print("จำนวนสินค้าที่ลดต้องมากกว่า 0")

    # แก้ไขราคา
    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price
            print(f"- ปรับราคา {self.name} เป็น {self.price} บาทสำเร็จ")
        else:
            print("ราคาต้องมากกว่า 0 บาท")

    # ตรวจสอบ
    def check_product_info(self):
        return f"ชื่อสินค้า: {self.name}\nราคา: {self.price} บาท\nสินค้าในสต๊อก: {self.__stock} ชิ้น"

class Phone(Product):
    def __init__(self, name, price, stock, phone):
        super().__init__(name, price, stock)
        self.phone = phone

    def check_product_info(self):
        return f"หมวดหมู่: {self.phone}\n{super().check_product_info()}"


class Notebook(Product):
    def __init__(self, name, price, stock, notebook):
        super().__init__(name, price, stock)
        self.notebook = notebook

    def check_product_info(self):
        return f"หมวดหมู่: {self.notebook}\n{super().check_product_info()}"


class Costume(Product):
    def __init__(self, name, price, stock, costume):
        super().__init__(name, price, stock)
        self.costume = costume

    def check_product_info(self):
        return f"หมวดหมู่: {self.costume}\n{super().check_product_info()}"


# เพิ่มสินค้า ชื่อ ไม้เเบดมินตัน VS Titan9 ราคา 1490 ในสต๊อกมี 30
product1 = Product("ไม้เเบดมินตัน VS Titan9", 1490, 30)
product1.add_stock(30)
product1.update_price(1590)
print("--------------------------------")
phone1 = Phone("Vivo", 5999, 40, "โทรศัพท์")
notebook1 = Notebook("Acer", 20000, 25, "โน๊ตบุ๊ค")
costume1 = Costume("เสื้อวอร์ม", 200, 90, "เสื้อผ้า")

# แสดงผลข้อมูลสินค้า
print(product1.check_product_info())
print("--------------------------------")
print(phone1.check_product_info())
print("--------------------------------")
print(notebook1.check_product_info())
print("--------------------------------")
print(costume1.check_product_info())
print("--------------------------------")

