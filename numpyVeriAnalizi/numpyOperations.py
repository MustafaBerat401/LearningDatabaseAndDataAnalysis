import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)


print(numbers1)
print(numbers2)

result = numbers1+numbers2 # iki dizinin aynı indexteki elemanlarını toplar.
result = numbers1 + 10 # her bir elemanın üzerine 10 ekler
result = numbers1-numbers2
result = numbers1-10
result = numbers1*numbers2
result = numbers1*10
result = numbers1/numbers2
result = numbers1/10

result = np.sin(numbers1) # her bir indexin sinüsünü alır
result = np.cos(numbers1)
result = np.sqrt(numbers1) # her bir elemanın karekökünü alır
result = np.log(numbers1)


multiNumbers1 = numbers1.reshape(2,3)
multiNumbers2 = numbers2.reshape(2,3)

# print(multiNumbers1)
# print(multiNumbers2)

result = np.vstack((multiNumbers1,multiNumbers2)) # dikey olarak birleştiri
result = np.hstack((multiNumbers1,multiNumbers2)) # yatay olarak birleştiri

result = numbers1 >= 25
result = numbers1 %2 == 0


print(numbers1[result])




# print(result)







