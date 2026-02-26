print("1 dan 10 gacha:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

print("Juft raqamlar (1-20):")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

for i in range(1, 6):
    print(f"gacha bo'lgan kvadrati: {i**2}")

matn = "Python"
for harf in matn:
    print(harf)

son = int(input("Biror raqam kiriting: "))
for i in range(1, 11):
    print(f"{son} * {i} = {son * i}")

yigindi = 0
for i in range(1, 101):
    yigindi += i
print(yigindi)

ismlar = ["Aziz", "Buni", "islom", "Shoh"]
for ism in ismlar:
    print(ism)

for i in range(10, 0, -1):
    print(i)
