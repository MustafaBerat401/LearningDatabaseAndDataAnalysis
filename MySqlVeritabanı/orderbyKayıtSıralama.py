import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="node-app")
    cursor = connection.cursor()


    # cursor.execute("Select * From Products Order By name") # isme göre sıralama işleme yaptık.
    # cursor.execute("Select * From Products Order By price") # fiyata göre sıralama işlemi yaptık.
    # cursor.execute("Select * From Products Order By id") # id'ye göre sıralama işlemi yaptık.
    # cursor.execute("Select * From Products Order By id DESC") # id'ye göre tersten sıralama işlemi yaptık.
    # cursor.execute("Select * From Products Order By price DESC ") # fiyata göre tersten sıralama işlemi yaptık.
    cursor.execute("Select * From Products Order By name,price") # isme ve fiyata göre sıralama işleme yaptık.
    
    try:
        result = cursor.fetchall()
        for product in result:
            print(f'id: {product[0]} name: {product[1]} price: {product[2]} ')
    except mysql.connector.Error as err:
        print('hata:',err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

    

getProducts()







