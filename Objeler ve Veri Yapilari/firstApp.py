# Örnek
"""
maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAli - (maasAhmet * vergi))

#**string ile number degiskenlerinin tanimlama farki
a = "10"
b= "20"
print(a + b);

firstName = "Ferhat "
lastName = "Dövme "
print(firstName + lastName)
"""

# **Veri dönüsümleri####
# x = input("1. Sayi: ")
# y = input("2. Sayi ")

# print(type(x))

# toplam = int(x) + int(y)
# print(toplam)

# ** ÖRNEK Kodlama
# yari capi verilen bir dairenin alan ve cevresini hesaplayiniz (r:3.14)
"""
pi = 3.14

r = float(input("yari cap: "))
# ** ile sayinin karesi aliniyor
alan = pi * (r**2)
cevre = 2 * pi * r

print("Alan:", alan)
print("Cevre:", cevre)
#! yada 
print("alan: " + str(alan) + " cevre: " + str(cevre))"""

"""greeting = "My name is Ferhat and this is a example"
print(len(greeting))
print(greeting[1:4])
print(greeting[:17])
"""

# * Stringleri formatlama
"""name = "Ferhat"
surname = "Dövme"
age = "33"
print("My name is {} {}".format(name, surname))


degisik yazma sekilleri
print("My name is {0} {1}".format(name, surname))  
print("My name is {1} {0}".format(name, surname))  
print("My name is {s} {n}".format(n=name, s=surname))  

result = 200/ 700
#! virgülden sonra kac basamak yazdirmak istersek
print ("the result is {r:1.4}".format(r=result))

#! bu yöntemin en kisa yolu ise parantez icine ilk olarak f yazmak
print(f"My Name is {name} {surname} and I'm {age} years old ")
"""

