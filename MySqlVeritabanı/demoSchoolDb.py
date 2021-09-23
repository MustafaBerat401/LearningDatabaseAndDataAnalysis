# 1- Workbench IDE ile schooldb isminde bir database oluşturup
#    Student tablosunu ekleyiniz. Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz.

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

    # ("101","Ahmet","Yılmaz",datetime.datetime(2005,5,17),"E"),
    # ("102","Ali","Can",datetime.datetime(2005,6,17),"E"),
    # ("103","Canan","Tan",datetime.datetime(2005,7,7),"K"),
    # ("104","Ayşe","Taner",datetime.datetime(2005,9,23),"K"),
    # ("105","Bahadır","Toksöz",datetime.datetime(2004,7,27),"E"),
    # ("106","Ali","Cenk",datetime.datetime(2003,8,25),"E")
"""
import mysql.connector
from datetime import datetime 
from connection import connection

class Student:
    connection = connection
    cursor = connection.cursor()
    def __init__(self,studentnumber,name,surname,birthdate,gender):
        self.studentnumber = studentnumber
        self.name = name
        self.surname = surname
        self.birthdate =birthdate
        self.gender = gender
    
    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentnumber,self.name,self.surname,self.birthdate,self.gender)
        Student.cursor.execute(sql,value)
        
        try:
            Student.connection.commit()
            print(f'{Student.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata: ',err)
        finally:
            Student.connection.close()
            print('database bağlantısı kapandı')
    
    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.cursor.executemany(sql,values)
        
        try:
            Student.connection.commit()
            print(f'{Student.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata: ',err)
        finally:
            Student.connection.close()
            print('database bağlantısı kapandı')
# ahmet = Student("202","ahmet","yılmaz",datetime(2005,5,17),"E")
# ahmet.saveStudent()
ogrenciler = [
    ("301","Ahmet","Yılmaz",datetime(2005,5,17),"E"),
    ("302","Ali","Can",datetime(2005,6,17),"E"),
    ("303","Canan","Tan",datetime(2005,7,7),"K"),
    ("304","Ayşe","Taner",datetime(2005,9,23),"K"),
    ("305","Bahadır","Toksöz",datetime(2004,7,27),"E"),
    ("306","Ali","Cenk",datetime(2003,8,25),"E")
]
Student.saveStudents(ogrenciler)
"""
# 4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 doğumlu öğrenci bilgilerini alınız.
#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız.
#   g- Kaç erkek öğrenci vardır?
#   h- Kız öğrencileri harf sırasına göre getiriniz.

# 5- Aşağıdaki güncelleme sorularını yazınız.
#   a- id'e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet'e göre aldığınız bir öğrencinin bilgilerini

import mysql.connector
from datetime import datetime 
from connection import connection

class Student:
    connection = connection
    cursor = connection.cursor()
    
    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
            
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.cursor.execute(sql,value)
        
        try:
            Student.connection.commit()
            print(f'{Student.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata: ',err)
        finally:
            Student.connection.close()
            print('database bağlantısı kapandı')
    
    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.cursor.executemany(sql,values)
        
        try:
            Student.connection.commit()
            print(f'{Student.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata: ',err)
        finally:
            Student.connection.close()
            print('database bağlantısı kapandı')
    
    @staticmethod
    def studentInfo():
        sql = 'SELECT * FROM Student' 
        sql = 'SELECT * FROM Student LIMIT 5' # tüm kayıtların ilk 5 tanesini getirir. 
        # sql = 'SELECT StudentNumber,Name,Surname FROM Student'
        # sql = "Select Name,Surname from student Where Gender='K' "
        # sql = "Select * from student where YEAR(Birthdate)=2003 "
        # sql = "Select * from student Where YEAR(Birthdate)=2005 and Name='Ali' "
        # sql = "Select * from student Where Name LIKE '%an%' or Surname LIKE '%an%' "
        # sql = "Select COUNT(*) from student Where Gender='E' " # bu sorguda fetchone() kullanmamız gerekmektedir.
        # sql = "Select Name,Surname from student Where Gender='K' order by name,surname "

        Student.cursor.execute(sql)

        try:
            results = Student.cursor.fetchall()
            
            for result in results:
                print(f'{result}')

        except mysql.connector.Error as err:
            print('hata',err)
        finally:
            Student.connection.close()

    @staticmethod
    def getStudentById(id):
                
        sql = "Select * From student Where id =%s"
        value= (id,)
        
        Student.cursor.execute(sql,value)

        try:
            obj = Student.cursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print('Hata:',err)
        
    
    def updateStudent(self):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.cursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f' {Student.cursor.rowcount} tane kayıt güncellendi. ')
        except mysql.connector.Error as err:
            print('Hata:',err)

    @staticmethod
    def updateStudents(liste):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.cursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f' {Student.cursor.rowcount} tane kayıt güncellendi. ')
        except mysql.connector.Error as err:
            print('Hata:',err)

    @staticmethod
    def getStudentsGender(gender):
                
        sql = "Select * From student Where gender =%s"
        value= (gender,)
        
        Student.cursor.execute(sql,value)

        try:
            return Student.cursor.fetchall()
        except mysql.connector.Error as err:
            print('Hata:',err)
        

# student = Student.getStudentById(10)

# student.name='Çınar'
# student.surname='Turan'

# student.updateStudent()

students = Student.getStudentsGender('E')
print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = 'Mr ' + std[2]
    liste.append(std)

Student.updateStudents(liste)








