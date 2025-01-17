import mysql.connector
class Managerdb:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.mycursor = self.mydb.cursor()

    def selectdb(self, table):
        sql = f"SELECT * FROM {table}"
        self.mycursor.execute(sql) 
        show = self.mycursor.fetchall()
        return show
    
#--------------------------------------------------------------------------------# 
#    
    def deletdb(self,table, id, id_name):
        sql = f"DELETE FROM {table} WHERE {id_name} = {id}"
        self.mycursor.execute(sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
        
#--------------------------------------------------------------------------------# 

    def editdb(self, table, column, id_name,id,val):
        sql = f"UPDATE {table} SET {column} = %s WHERE {id_name} = %s"
        val_sql = (val,id)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
#--------------------------------------------------------------------------------

    def insert_categories(self, name):  # เปลี่ยนชื่อเป็น categories
        sql = "INSERT INTO categories (category_id,category_name) VALUES (%s, %s)"
        val_sql = (None, name)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False 
        
    def insert_user(self, name,password,email,role):
        sql = "INSERT INTO user VALUES (%s,%s,%s,%s,%s)"
        val_sql = (None, name,password,email,role)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
        
    def insert_orders(self, date,amount,status):
        sql = "INSERT INTO orders VALUES (%s, %s,%s,%s)"
        val_sql = (None,date,amount,status)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
        
    def insert(self, name,des,price,stock):
        sql = "INSERT INTO product VALUES (%s, %s, %s, %s, %s)"
        val_sql = (None, name,des,price,stock)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
#--------------------------------------------------------------------------------
#ลองเรียกใช้
result_select = Managerdb('localhost','root','1234','shop')

#ลบ
#print(result_select.deletdb('products', 'product_id', 112))

#เรียกดู
#print(result_select.selectdb('products'))

#ลบ
#print(result_select.deletdb('products', 'product_id', 112))

#เเก้ไข
#print(result_select.editdb('categorie', 'category_name', 'category_id', 2223, 'ไม้กอล์ฟ'))

#เพิ่มข้อมูล
print(result_select.insert_categories('ไม้เปตอง'))