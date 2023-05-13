# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 19:19:49 2023

@author: Sozla.uz
8_dars python
autor -->>> Istamov Mirjahon
"""
#SORT funfsiaysi ingliz alifbosi tartibida qaytaradi B a dan oldin keladi 
cars = ["bmv", "audi", "lambargini", "ferrari"]
#cars.sort()
#print(cars)
 
#sorted funksiyasi teskarisini qaytaradi
#print(sorted(cars ,reverse=True))

#cars.reverse() #bu qiymatni aylantirib quyadi
#print(cars)

#LEN funksiyasi uzunligini ulchab beradi
#uzunlik = len(cars)
#print(uzunlik)
#cars.sort(reverse=True)
#print(cars)

#range 
sonlar = list(range(0,20)) # 0 dan 20 gacha sonlarn chiqaradi 20 mani ciqarmaydi
#rint(sonlar)

juft_sonlar = list(range(1,20,2))
toq_sonlar = list(range(1,20,2))
#print(juft_sonlar)
#print(toq_sonlar)

#MAX funfsiyasi
maksimal = max(juft_sonlar)
#print(maksimal)

narxlar = [12000, 1300, 34256, 345, 4353, 34434]
#print("Narxlar orasidagi max:",max(narxlar))
#print("Narxlar orasidagi min:", min(narxlar))
#print("Narxlar summasi:", sum(narxlar))

#RUYXATNI KESIB OLISH -->> ":"
#print(cars) 
#print(cars[0:3]) # 0,1,2 chi indekslargadilarni ciqaradi 
#print(cars[1:])  # 1-indeksdan bowlab oxirigacha chiqaradi  
#print(cars[:2])


#my_cars = cars
#my_cars.remove('audi')
#my_cars[0] =("Malibu")
#print(my_cars)
#print(cars)

#Nusxalash uchun [:] ishlatiladi
my_cars = cars[:]
my_cars.remove('audi')
my_cars[0] =("Malibu")
print(my_cars)
print(cars)


#tuple() bu uzgarmas ruyxat bunga quwib ham uchirib ham bulmaydi

toys = ('bear', 'snake', 'rabbit', 'car')
toys = list(toys)
toys.remove('snake')
toys.append('teddy')
print(toys)
toys = tuple(toys)
#tuole funksiyasiga remove ni ishlatib bulmaydi
print(toys)











