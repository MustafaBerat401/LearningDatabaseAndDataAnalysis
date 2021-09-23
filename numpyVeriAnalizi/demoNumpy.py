# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.

import numpy as np

# numbers1 = np.array([10,15,30,45,60])
# print(type(numbers1))

# # 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.

# result = np.arange(5,15)
# print(result)


# # 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
# result = np.arange(50,100,5)
# print(result)

# # 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
# result = np.zeros(10)
# print(result)

# # 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
# result = np.ones(10)
# print(result)

# # 6- (0-100) arasında eşit aralıklı 5 sayı üretin.

# result = np.linspace(0,100,5)
# print(result)


# # 7- (10-30) arasında rastgele 5 tane tamsayı üretin
# result = np.random.randint(10,30,5)
# print(result)


# # 8- [-1 ile 1] arasında 10 adet sayı üretin.
# result = np.random.randn(10)
# print(result)

# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
# result = np.random.randint(10,50,15).reshape(3,5)
# print(result)

# # 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız.
# matris = np.random.randint(10,50,15).reshape(3,5)
# rowTotal = matris.sum(axis = 1)
# colTotal = matris.sum(axis = 0)
# print(matris)
# print(rowTotal)
# print(colTotal)

# # 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir?
# matris = np.random.randint(10,50,15).reshape(3,5)
# print(matris)
# enBuyuk = matris.max()
# enKucuk = matris.min()
# ortalama = matris.mean()
# print(f"En büyük sayı=>{enBuyuk}\nEn küçük sayı=>{enKucuk}\nOrtalama=>{ortalama} ")



# # 12- Üretilen matrisin en büyük değerinin indeksi kaçtır = ?
# matris = np.random.randint(10,50,15).reshape(3,5)
# print(matris)
# enBuyukIndex = matris.argmax()
# enKucukIndex = matris.argmin()
# print(f"En büyük sayının index numarası=>{enBuyukIndex}\nEn küçük sayının index numarası=>{enKucukIndex}")


# # 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz
# arr = np.arange(10,20)
# result = arr[0:3]
# result = arr[:3]
# print(result)


# # 14- Üretilen dizinin elemanlarını tersten yazdırın.
# arr = np.arange(10,20)
# result = arr[::-1]
# print(result)


# # 15- Üretilen matrisin ilk satırını seçiniz.
# matris = np.random.randint(10,50,15).reshape(3,5)
# print(matris[0])


# # 16- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir?
# matris = np.random.randint(10,50,15).reshape(3,5)
# print(matris)
# print(matris[1][2])
# print(matris[1,2])


# # 17- Üretilen matrisin tüm elemanlarındaki ilk elemanı kaçtır?
# matris = np.random.randint(10,50,15).reshape(3,5)
# print(matris)
# print(matris[:,0])

# # 18- Üretilen matrisin her bir elemanının karesini alınız.
# matris = np.random.randint(10,50,15).reshape(3,5)
# print(matris)
# result = np.square(matris)
# result = matris ** 2
# print(result)


# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır?
#     Aralığı(-50,+50) arasında yapınız.
matris = np.random.randint(-50,50,15).reshape(3,5)
print(matris)
ciftler = matris[matris %2 == 0]
result = ciftler[ciftler>0]
print(result)













