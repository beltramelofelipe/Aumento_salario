salario = float(input('Digite seu salario: '))
if (salario > 1250):
  print('O novo salario será de R$ {} com reajuste de 10%'.format(salario + (salario * 0.1)))
else:
  print('O novo salario será de R$ {} com reajuste de 15%'.format(salario + (salario * 0.15)))