# tento program vypočíta obvod a obsah štvorca

strana = float(input('Zadaj stranu štvorca v cemtimetroch: '))

print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')

def obsah_obdelnika(a, b):
    return a * b

a = float(input('Zadaj stranu a obdĺžnika: '))
b = float(input('Zadaj stranu b obdĺžnika: '))
print('Obsah obdélníka se stranami ', a, ' cm a ', b, ' cm je', obsah_obdelnika(a, b), 'cm2')
