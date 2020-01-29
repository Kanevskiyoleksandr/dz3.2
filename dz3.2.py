print("ВВедите значение А")
a = int(input())
print("Введите значение B")
b = int(input())
print("Введите значение V")
v = int(input())
while a < b:
    print(a)
    print("Пока что нет")
    a = a + v
if a > b:
    print(a)
    print("Дождались!")
