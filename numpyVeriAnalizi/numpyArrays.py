import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10) # 1 ile 10 arasında bir dizi oluşturur
# result = np.arange(10,100,3) # 10dan başla 100e kadar 3er 3er git.
# result = np.zeros(10) # 10 tane sıfırı verir.
# result = np.ones(10) # 10 tane biri verir.
# result = np.linspace(0,100,5) # başlangıç(0) ve bitiş(100) değerlerini eşit aralıklarla böler
# result = np.linspace(0,5,5)
# result = np.random.randint(0,10) # 0 ile 10 arasında rastgele bir sayı üretir.(10 dahil değil)
# result = np.random.randint(20) # sadece bitiş değeri de verilebilir.Varsayılan olarak sıfırdan başlar.
# result = np.random.randint(1,10,3) # 1 ile 10 arasında farklı 3 tane sayı geitirir.
# result = np.random.rand(5) # 0 ile 1 arasında rastgele 5 sayı üretir
# result = np.random.randn(5) # negatif değerler de işin içine katılır
np_array = np.arange(50) # 0'dan 50'ye kadar olan sayıları yazdırır 50 dahil değil
np_multi = np_array.reshape(5,10) # 5x10'luk matris oluşturur.
# print(np_multi.sum(axis=1)) # satırların toplamını yapar.
# print(np_multi.sum(axis=0)) # sütunların toplamını yapar


# rnd_numbers = np.random.randint(1,100,10)
# print(rnd_numbers)
# result = rnd_numbers.max() # üretilen sayılardan en büyüğünü alır
# result = rnd_numbers.min() # üretilen sayılardan en küçüğünü alır
# result = rnd_numbers.mean() # üretilen sayıların ortalamasını verir.
# result = rnd_numbers.argmax() # üretilen en büyük sayının index numarasını verir
# result = rnd_numbers.argmin() # üretilen en küçük sayının index numarasını verir

print(np_multi)


