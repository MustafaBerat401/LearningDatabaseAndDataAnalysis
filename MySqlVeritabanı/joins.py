
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

    # sql = "Select * from products"
    # sql = "Select * from categories"
    # sql = "Select * From Products inner join Categories on Categories.id=Products.Categoryid" # telefon olanları telefonların idlerine pc olanları pclerin idlerine göre eşleştirip join işlemi yaptık.
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid"
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid where Categories.name='Telefon'"
    sql = "Select p.name,p.price,c.name From Products as p inner join Categories as c on c.id=Products.p where p.name='Samsung S8'" # Product => p olarak Category => c olarak isimlendirdik takma isim koyduk
    
    
    cursor.execute(sql)
    try:
        result = cursor.fetchall() 
        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print('hata:',err)
    finally:
        connection.close()

getProducts()
