import numpy as np


numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
result = numbers[-1]
result = numbers[0:3]
print(result)
result = numbers[:3]
result = numbers[3:]
result = numbers[::]
result = numbers[::-1]
result = numbers[::-2]

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numbers2[0]
result = numbers2[2]
result = numbers2[0,2]
result = numbers2[2,2]
result = numbers2[:,2] # tüm satırlardaki 2.indexler alınır.
result = numbers2[:,0] # tüm satırlardaki 0.indexler alınır.
result = numbers2[:,0:2] # tüm satırlardaki 0dan 2.indexe kadar olan indexleri yazdırır
result = numbers2[-1,:] # son satırı alır.
result = numbers2[:2,:2]

# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1 # referans kopyalama yapmış olduk

arr2 = arr1.copy()

arr2[0] = 20

print(arr1)
print(arr2)




