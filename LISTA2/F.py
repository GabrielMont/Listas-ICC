inp = input()
h1, m1, h2, m2 = [int(x) for x in inp.split()]

dh = h2 - h1
if dh <= 0:
    dh = 24 - dh

dm = m2 - m1
if dm < 0:
    dm = 60 + dm
    dh -= 1

print('O jogo durou %d hora(s) e %d minuto(s).' % (dh, dm))
