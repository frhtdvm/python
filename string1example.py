website = "https://www.sadikturan.com"
course = "Python Kursu: Bastan sona Python Programlama Rehberiniz (40 Saat)"

# 1 course karakter dizisinin uzunlugu nedir
print(len(course))
length = len(website)
# 2 websitesi icinden www karakterlerini alin
print(website[8:11])
# 3 websitesi icinden com karakterlerini alini
print(website[23:26])
print(website[length - 3 : length])
# 4 course icinden ilk ve son 15 karakteri alin
print(course[0:15])
print(course[-15:])
# 5 course ifadesindeki karakteri tersten yazdirin
#!-> :: ile tüm karakterler yazdirilir, -1 ile de sagdan sola git diyoruz
print(course[::-1])

# 6 Benim adim Bora Yilmaz, yasim 32 ve meslegim mühendislik i yazdiriniz

name, surname, age, job = "Bora", "Yilmaz", 32, "mühendis"

print(f"Benim adim {name} ve soyadim {surname} {age} yasindayim ve Meslegim {job}")
# 7 "Hello world" deki w yi W ile degistirin
s = "Hello world"
s = s[0:6] + 'W' + s[-4:]
print(s)
#! yukardaki parcala ve yeni harf ekleme teknigi ile harf degistirildi 
# 8 abc ifadesini yan yana 3 kez yazdirin 
result = "abc" * 3
print(result)