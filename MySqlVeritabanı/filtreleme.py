import mysql.connector


def insertProduct(name,price,imageUrl,description):
    connection = mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)
    
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid} ')
    except mysql.connector.Error as err:
        print('hata:',err)
    finally:
        connection.close()
        print('database bağlantısı kapandı')



def insertProducts(list):
    connection = mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list
    
    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid} ')
    except mysql.connector.Error as err:
        print('hata:',err)
    finally:
        connection.close()
        print('database bağlantısı kapandı')


def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="node-app")
    cursor = connection.cursor()

    # cursor.execute('Select * From Products Where id=1') # where komutu filtre yapmamızı sağlar. Burada id'si sadece 1 olan kayıtları getir dedik.
    # cursor.execute("Select * From Products Where name='Samsung S7'") # isme göre filtreledik
    # cursor.execute("Select * From Products Where name='Samsung S7' and price=3000") # isim ve fiyata göre filtreleme işlemi yaptık.
    # cursor.execute("Select * From Products Where name='Samsung S7' and price>=3000")
    # cursor.execute("Select * From Products Where name='Samsung S7' or price>=3000")
    # cursor.execute("Select * From Products Where name LIKE '%Samsung%' ") # aradığımız kelimenin name alanı içerisinde herhangi bir yerinde geçiyorsa o kayıtları getir demektir.
    # cursor.execute("Select * From Products Where name LIKE 'Samsung%' ") # başı samsung olup sonu ne olursa olsun farketmez o kayıtları getirir.
    # cursor.execute("Select * From Products Where name LIKE '%Samsung' ") # başı ne olursa olsun farketmez ama sonu samsung olan kayıtları getirir.
    # cursor.execute("Select * From Products Where name LIKE '%Samsung%' and price=3000 ")
    cursor.execute("Select * From Products Where id = 1 ")
    
    '''
    fetchone() ile fetchall() arasındaki fark;
    fetchone() komutu tek bir kayıt getirirken bunu liste şeklinde getirmez yani tek bir kayıt
    alınacaksa bunu fetchone() ile yaparız ve yazdırırken for döngüsüyle uğraşmayız.
    fetchall() ise tek kayıtta gelse birden fazla kayıtta gelse her türlü liste şeklinde getirir.
    yani bu fetchall()'u kullanıyorsak for döngüsüyle bu kayıtları yazdırmamız gerekir.
    '''
    result = cursor.fetchone() 
    print(f'id: {result[0]} name: {result[1]} price: {result[2]} ')


    # for product in result:
    #     print(f'id: {product[0]} name: {product[1]} price: {product[2]} ')


def getProductById(id):
    connection = mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="node-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id =%s"
    params= (id,)
    cursor.execute(sql,params)

    result = cursor.fetchone() 
    print(f'id: {result[0]} name: {result[1]} price: {result[2]} ')

getProductById(3)

