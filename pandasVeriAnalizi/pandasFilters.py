import pandas as pd
import numpy as np


data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5"])

result = df
result = df.columns # verinin kolon bilgilerini alır.
result = df.head() # ilk beş satırı getirir
result = df.head(10) # ilk 10 satırı getirir
result = df.tail() # sondan 5 satır gelir
result = df.tail(10) # sondan 10 satırı getirir.
result = df["Column1"].head() # 1.kolonun ilk beş satırını getirir.
# result = df.Column1.head()
result = df[["Column1","Column2"]].head() # sadece kolon1 ve kolon2 nin ilk beş satırını alır.
result = df[["Column1","Column2"]].tail() # sadece kolon1 ve kolon2 nin sondan beş satırını alır.
result = df[5:15][["Column1","Column2"]].head() # 5 ile 15 arasındaki kayıtların 1. ve 2.kolonlarının ilk 5 tanesini getir.
result = df[5:15][["Column1","Column2"]].tail() # 5 ile 15 arasındaki kayıtların 1. ve 2.kolonlarının sondan 5 tanesini getir.

result = df > 50 # 50den büyük olan sayılar varsa true döndürür yoksa false
result = df[df > 50] # 50den büyük olan kayıtları gösterir diğerlerini göstermez
result = df[df % 2 == 0]
result = df["Column1"] > 50 # 1.kolondaki 50 den büyük olan sayıları true false döndürür.
result = df[df["Column1"] > 50] # true false değil de konsola sayıları yazdırmak için bu şekilde bi yöntem uygulanır.
result = df[df["Column1"] > 50][["Column1","Column2"]]
result = df[(df["Column1"] > 50) & (df["Column1"]<=70)] # kolon1 in hem 50den büyük hemde 70e küçük ve eşit olan sayıların getirilişi
result = df[(df["Column1"] > 50) & (df["Column2"]<=70)] # kolon1 50den büyük ve aynı zamanda kolon2 70den küçük ve eşit olacak
result = df[(df["Column1"] > 50) | (df["Column2"]<=70)] # koşullardan sadece bir tanesinin doğru olması yeterli yani kolon1 50den büyükse veya kolon2 70den küçük ve eşitse ikisinden birini veya ikisini de yazdır.
result = df.query("Column1 >= 50 & Column1 % 2 == 0") # filtreleme işlemlerini query ile de yapablilriz.
result = df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]]
result = df.query("Column1 >= 50 | Column1 % 2 == 0")[["Column1","Column2"]]

print(result)















