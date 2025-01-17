import database 
mycursor = database.mydb.cursor()
def selectdb(table):
    sql = f"SELECT * FROM {table}"
    mycursor.execute(sql)
    show = mycursor.fetchall()
    return show
#print(selectdb('users'))
#--------------------------------------------------------------------------------#
def deletdb(table,id,id_name):
    sql = f"DELETE FROM {table} WHERE {id_name} = {id}"
    mycursor.execute(sql)
    database.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False

#print(deletdb("categories","product_id",112))
#--------------------------------------------------------------------------------#

def editdb(table,colum,id_name,val):
    sql = f"UPDATE {table} SET {colum} = %s WHERE {id_name} = %s"
    val_sql = {val,id_name}
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
    
#print(editdb("product","stock_product","product_id",8,"ไม้เเบดมินตัน Vstitan7"))
#--------------------------------------------------------------------------------#

def insert_categories(name):
    sql = "INSERT INTO categories VALUES (%s , %s)"
    val_sql = (None,name)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
    
#print(insert_categories("ไม้เปตอง"))
#--------------------------------------------------------------------------------#