def imc(altura, peso):
  result = peso / (altura * altura)
  match result:
    case result if (result < 17):                        print("\033[1;31m" + '\n' + 'Muito abaixo do peso')
    case result if (result >= 17 and result <= 18.49):   print("\033[1;33m" + '\n' + 'Abaixo do peso')
    case result if (result > 18.49 and result <= 24.99): print("\033[1;32m" + '\n' + 'Peso Normal')
    case result if (result > 24.99 and result <= 29.99): print("\033[1;33m" + '\n' + 'Acima do peso')
    case result if (result > 29.99 and result <= 34.99): print("\033[1;31m" + '\n' + 'Obesidade I')
    case result if (result > 34.99 and result <= 39.99): print("\033[1;31m" + '\n' + 'Obesidade II (Severa)')
    case result if (result > 39.99):                     print("\033[1;31m" + '\n' + 'Obesidade III (Mórbida)')

print("\033[1;36m" + 'CALCULO IMC' + '\n')
print("\033[0;0m") # Reset color 
altura = float(input('Digite sua altura: '))
peso =   float(input('Digite seu peso: '))

imc(altura, peso)
print("\033[0;0m")
