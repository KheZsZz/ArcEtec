import random

quiz = [
  {'Pergunta':'A', 'r1': 'p1', 'r2':'nn', 'r3':'nn', 'r4':'nn'},
  {'Pergunta':'A', 'r1': 'p1', 'r2':'nn', 'r3':'nn', 'r4':'nn'},
  {'Pergunta':'A', 'r1': 'p1', 'r2':'nn', 'r3':'nn', 'r4':'nn'},
  {'Pergunta':'A', 'r1': 'p1', 'r2':'nn', 'r3':'nn', 'r4':'nn'},
  {'Pergunta':'A', 'r1': 'p1', 'r2':'nn', 'r3':'nn', 'r4':'nn'},
  {'Pergunta':'A', 'r1': 'p1', 'r2':'nn', 'r3':'nn', 'r4':'nn'},
  {'Pergunta':'A', 'r1': 'p1', 'r2':'nn', 'r3':'nn', 'r4':'nn'},
  {'Pergunta':'A', 'r1': 'p1', 'r2':'nn', 'r3':'nn', 'r4':'nn'},
  {'Pergunta':'A', 'r1': 'p1', 'r2':'nn', 'r3':'nn', 'r4':'nn'},
  {'Pergunta':'A', 'r1': 'p1', 'r2':'nn', 'r3':'nn', 'r4':'nn'},
]

contador = 0
i = 0 # Indice
corInd = 1;
count = list(range(1,5)) # cria uma lista de 1 a 4

for pergunta in quiz: #Percorre o Array de perguntas
  i = i + 1 # soma +1 no indice
  print(
    "\033[1;96m"+
    '\n'
    '{}° Pergunta: {} \n'
    .format(i, pergunta.get('Pergunta'))
  ) # Mostra a pergunta

  al = list(range(1,5)) # cria uma lista de 1 a 4

  for x in count:
    random.shuffle(al) # embaralha a lista deixando ela aleatória
    ind = al.pop() # Tira um item da lista embaralhada.
    
    print(
      "\033[1;97m"+
      '{}) {}\r'
      .format(x, pergunta.get('r'+ str(ind) ))
    ) # mostra as opç~es com as respostas embaralhadas
    
    if(ind == 1):
      corInd = x
      
  resposta = int(input('Resposta: ')) # Pega a resposta do usuário
  
  if(resposta == corInd): #veficia se a resposta do usuario é igual ao indice da resposta
    
    print(
      "\033[1;32m" +
      '\n'
      'Acertou!!!'
      '\n'
    ) #mostra se acertou
    contador = contador + 1 #soma +1 no contador de perguntas acertadas
    
  else: #Caso nn tenha acertado
    
    print(
      "\033[1;31m" + 
      '\n'
      'Errou!!!'
      '\n'
    ) #mostra que errou
    
print(
  "\033[1;93m"+
  'Você acertou {}/10 perguntas'
  .format(contador)
) #mostra a quantidade que acertou...

## Verifica a categoria de acertos.
if contador >= 9:
    print('Você é um expert no assunto')
if contador >= 7 and contador <= 8:
    print('Você tem um bom conhecimento no assunto')

if contador >= 5 and contador <= 6:
    print('Você tem um certo conhecimento no assunto')

if contador >= 3 and contador <= 4:
    print('Seu conhecimento é básico')

if contador >= 0 and contador <= 2:
    print('Você é um noob nesse assunto')

print("\033[0;0m") # Reset a cor do console
