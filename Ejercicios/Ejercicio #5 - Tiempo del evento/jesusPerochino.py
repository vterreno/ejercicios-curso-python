dia = input()
w1 = int(dia[-2:])
hora1 = input()
h1 = int(hora1[0:2])
m1 = int(hora1[5:7])
s1 = int(hora1[-2:])
dia2 = input()
w2 = int(dia2[-2:])
hora2 = input()
h2 = int(hora2[0:2])
m2 = int(hora2[5:7])
s2 = int(hora2[-2:])

diap = w2 - w1
hp = h2 - h1
mp = m2 - m1
sp = s2 - s1

while sp < 0:
	mp -=1
	sp += 60
while mp < 0:
	hp -= 1
	mp += 60
while hp < 0:
	diap -= 1
	hp += 24

print(diap, "dia(s)")
print(hp, "hora(s)")
print(mp, "minuto(s)")
print(sp, "segundo(s)")