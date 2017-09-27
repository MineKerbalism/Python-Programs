daljina_pole = 50
broy_igrachi = 8 
pozicii = [1, 5, 3, 8, 9, 7, 4, 12]

for tekushta_poziciya in range(1, daljina_pole + 1):
    simvol_za_izvejdane = '_'

    for index_igrach in range(broy_igrachi):
        if tekushta_poziciya == pozicii[index_igrach]:
            simvol_za_izvejdane = str(index_igrach)
    print(simvol_za_izvejdane),