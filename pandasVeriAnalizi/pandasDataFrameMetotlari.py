import pandas as pd
import numpy as np

# data = {
#     "Column1": [1,2,3,4,5],
#     "Column2": [30,20,28,25,25],
#     "Column3": ["abc","bca","ade","cba","dea"]
# }

# df = pd.DataFrame(data)

# def kareal(x):
#     return x * x

# # kareal2 = lambda x: x*x

# result = df
# result = df["Column2"].unique() # tekrarlayan değerleri sadece bir kere yazdırır
# result = df["Column2"].nunique()
# result = df["Column2"].value_counts() # her bir elemanın kaç tane tekrarladdığını söyler
# result = df["Column1"] * 2
# result = df["Column1"].apply(kareal)
# # result = df["Column1"].apply(kareal2)
# # result = df["Column1"].apply(lambda x: x*x)
# df["Column4"] = df["Column3"].apply(len)
# result = df.columns
# result = len(df.columns)
# result = df.index
# result = len(df.index)
# result = df.info

# result = df.sort_values("Column2")
# result = df.sort_values("Column3")
# result = df.sort_values("Column3",ascending=False)


data = {
    "Ay":["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori":["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap"],
    "Gelir":[20,30,15,32,42,12]
}

df = pd.DataFrame(data)
result = df.pivot_table(index="Ay",columns="Kategori",values="Gelir")


print(result)




