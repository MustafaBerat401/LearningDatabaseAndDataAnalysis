import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"],columns=["Column1","Column2","Column3"])

result = df
result = df["Column1"] # 1. kolonu verir
result = type(df["Column1"])
result = df[["Column1","Column2"]]

# loc["row","column"] => loc["row"] sadece satır bilgisi
# loc["row","column"] => loc[:,"column"] sadece kolon bilgisi
result = df.loc["A"] # location metodu normal parantez içinde değil de köşeli parantez içinde kullanılır. Satırı verir.
result = type(df.loc["A"])
result = df.iloc[2] # iloc metodu indexleri değiştirmiş olsak bile 2. indexe karşılık gelen değerleri getirir.

# result = df.loc[:,["Column1","Column2"]]
# result = df.loc[:,"Column1":"Column3"] # Kolon1 ve kolon3 arasındaki tüm kolonları getir.
# result = df.loc[:,:"Column3"] # başlangıçtan itibaren başla ve kolon3e kadar git.
# result = df.loc["A":"B",:"Column2"] # A'dan başla B'ye kadar olan satırları getir ve 2. sütuna kadar da getir.
# result = df.loc[:"B",:"Column2"] # baştan B'ye kadar satırları getir.
result = df.loc["A","Column2"] # A satırının 2.kolondaki elemanını yazdırır.
result = df.loc["C","Column1"]
result = df.loc[["A","B"],["Column1","Column2"]] #A ve B satırlarının sadece 1. ve 2. kolondaki değerlerini getir.


df["Column4"] = pd.Series(randn(3),["A","B","C"]) # Yeni bir kolon ekledik
df["Column5"] = df["Column1"] + df["Column3"] # kolon1 ve kolon3'deki değerleri toplar ve yeni kolon5'i oluşturur.

# result = df.drop("Column5", axis = 1) # istediğimiz kolonu silmek için önce kolonun ismi ardından axisi yani yukarıdan aşağı olduğunu belirtmemeiz için axis'e 1 değeri tanımlanır.Lakin bunu yaptıktan sonra daha önceki orijinal dataframe'mizi güncellemez eski halinde kalır
# result = df.drop("Column5", axis = 1, inplace = True) # inplace'e true değerini atarsak önceki orijinal dataframe'mize de güncellemeyi yapar ve 5.kolon kalıcı olarak silinmiş olur.
result = df.drop("Column5", axis = 1, inplace = False) # orijinal üzerinde değişiklik yapılmadı sadece kopyası döndürüldü.

print(result)
print(df)







