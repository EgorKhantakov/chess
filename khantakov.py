a = 1
nskarea = 892000000000
#sm in square
weight = 0.000000005
capacity = 5*3*2
for i in range(64):
    a *=2
allcapacity = capacity*(a-1)
height = allcapacity/nskarea
allweight = (a-1)*weight
time = allweight/2600000
print("Зерен пшеницы:", a-1)
print("Масса зерна =", allweight,"тонн")
print("Высота слоя для Советского района НСК =", height/100, "м")
print("Время выращивания такого кол-ва зерна в НСК области =", time,"лет")

