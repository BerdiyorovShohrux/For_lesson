print("1 dan 5 gacha:")
i = 1
while i <= 5:
    print(i)
    i += 1

i = 10
while i >= 1:
    print(i,)
    i -= 1
  
print("Juftsonlar")
i = 2
while i <= 20:
    print(i,)
    i += 2

yigindi = 0
i = 1
while i <= 50:
    yigindi += i
    i += 1
print(yigindi)


soz = ""
while soz != "to'xtat":
    soz = input("Biror narsa yozing: ")



a, b = 0, 1
sanoq = 0
while sanoq < 5:
    print(a, end=" ")
    a, b = b, a + b
    sanoq += 1
print("\n")

son = -1
while son <= 0:
    m_son = int(input("son kiriting: "))
print(f"Siz {m_son} son kiritdingiz. u musbat")
