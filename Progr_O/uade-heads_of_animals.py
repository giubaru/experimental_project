cabezas = 35
patas = 94
i = 0
conejos = 0
while conejos <= cabezas:
    conejos += 1
    gallinas = cabezas - conejos
    if ((conejos*4)+(gallinas*2))==94:
        print("Hay %1d conejos y %1d gallinas" %(conejos, gallinas))