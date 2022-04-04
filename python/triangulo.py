
def typeIstriangle (ld1, ld2, ld3):
  if(ld1 <= 0 and ld2 <=0 or ld1 <= 0 and ld3 <= 0 or ld2 <= 0 and ld3 <= 0 or ld2 <= 0 and ld1 <= 0 or ld3 <=0 and ld1<=0): print('\n' + 'Reta')
  if(ld1 <= 0 and ld2 != 0 and ld3 != 0 or ld2 <= 0 and ld1 != 0 and ld3 != 0 or ld3 <= 0 and ld2 != 0 and ld1 != 0): print('\n' + 'Segmento de retas') 
  if(ld1 == ld2 and ld2 == ld3 and ld3 == ld1):print('\n' + 'EQUILÁTERO')
  if(ld1 == ld2 and ld3 != ld1 or ld2 == ld3 and ld1 != ld2 or ld3 == ld1 and ld2 != ld3):print('\n' + 'ISÓCELES')
  if(ld1 != ld2 and ld2 != ld3 and ld3 != ld1):print('\n' + 'ESCALENO')
 
 
 
ld1 = int(input('Digite o primeiro valor: '))
ld2 = int(input('Digite o segundo valor: '))
ld3 = int(input('Digite o terceiro valor: '))

typeIstriangle(ld1, ld2, ld3)