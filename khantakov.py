a = 1
b = 1
nskarea = 892000000000
#sm in square
weight = 0.000000005
capacity = 5*3*2
for i in range(63):
    a = a * 2
    b = b + a
allcapacity = capacity*(b)
height = allcapacity/nskarea
allweight = (b)*weight
time = allweight/2600000
print("Зерен пшеницы:", b)
print("Масса зерна =", allweight,"тонн")
print("Высота слоя для Советского района НСК =", height/100, "м")
print("Время выращивания такого кол-ва зерна в НСК области =", time,"лет")

