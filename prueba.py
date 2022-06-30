import random

phone = []
placa = []
tarifa = []

abcedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for i in range(10):
    template = '3'+str(random.randint(100000000, 299999999))
    phone.append(template)

for i in range(10):
    parte_letras = (random.choice(abcedario)+random.choice(abcedario)+random.choice(abcedario)).upper()
    parte_num = str(random.randint(000, 999))
    placa.append(parte_letras + parte_num)

for i in range(10):
    taf = str(random.choice([1000, 1500, 2000, 2500, 3000]))
    tarifa.append(taf)


for i in range(10):
    print(phone[i], placa[i], tarifa[i])
