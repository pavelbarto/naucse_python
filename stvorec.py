# tento program vypočíta obvod a obsah štvorca

# zadanie strany a skuska ci je kladna
strana = float(input('Zadaj stranu štvorca v cemtimetroch: '))
cislo_je_stravne = strana > 0

# priradenie hodnoty cisla pi
pi = 3.1415926

if cislo_je_stravne:
    print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
    print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
    print("Obvod kruhu s polomerom", strana, "je", 2 * pi * strana, "cm")
    print("Obsah kruhu s polomerom", strana, "je", pi * (strana * strana), "cm2")
else:
    print("Strana musi byt kladna, inak to nebude stvorec !")

print("Dakujeme za pouzitie geometrickej kalkulacky.")




def obsah_obdelnika(a, b):
    return a * b

a = float(input('Zadaj stranu a obdĺžnika: '))
b = float(input('Zadaj stranu b obdĺžnika: '))
print('Obsah obdélníka se stranami ', a, ' cm a ', b, ' cm je', obsah_obdelnika(a, b), 'cm2')
