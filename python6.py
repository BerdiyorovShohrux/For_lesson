son = float(input("Raqam kiriting: "))
if son > 0:
    print("Musbat")
elif son < 0:
    print("Manfiy")
else:
    print("Nol")

yosh = int(input("Yoshingizni kiriting: "))
if yosh >= 18:
    print("Siz kattasiz")
else:
    print("Siz voyaga yetmagansiz")

son = int(input("Butun son kiriting: "))
if son % 2 == 0:
    print("Juft son")
else:
    print("Toq son")

baho = int(input("Bahoni kiriting: "))
if baho >= 50:
    print("Imtihondan otdingiz")
else:
    print("Imtihondan otmadiz")

son = int(input("Son kiriting: "))
if son % 2 == 0 and son % 3 == 0:
    print("2ga ham 3ga ham bo'linadi")
else:
    print("To'gri son kirit")

gradus = float(input("Haroratni kiriting: "))
if gradus > 30:
    print("Issiq")
elif gradus < 10:
    print("Sovuq")
else:
    print("Iliq")


s1 = float(input("Birinchi son: "))
s2 = float(input("Ikkinchi son: "))
if s1 > s2:
    print("Kattasi:", s1)
elif s2 > s1:
    print("Kattasi:", s2)
else:
    print("Ular teng")

soz = input("Parolni kiriting: ")
if soz == "Python":
    print("To'g'ri!")
else:
    print("Qayta urinib ko'ring!")
