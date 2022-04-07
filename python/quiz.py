import random
theme = "Primeiros socorros / Corpo Humano"
quiz = [
  {
    'Pergunta':'Quantos ossos tem em média o corpo humano?', 
    'r1':'206 ossos', 
    'r2':'195 ossos', 
    'r3':'210 ossos', 
    'r4':'197 ossos'
  },
  
  {
    'Pergunta':'O que são artérias?', 
    'r1':'São vasos sanguíneos que garantem o transporte do sangue do coração para os diferentes tecidos do corpo', 
    'r2':'São vasos sanguíneos que garantem o transporte do sangue dos tecidos para o coração', 
    'r3':'São vasos que apresentam paredes finas', 
    'r4':'São vasos que transporta sangue em baixa pressão'
  },
  
  {
    'Pergunta':'Qual a maior artéria do corpo humano?', 
    'r1':'Artéria aorta', 
    'r2':'Artérias femorais:', 
    'r3':'Artérias carótidas', 
    'r4':'Artéria pulmonar'
  },
  
  {
   'Pergunta':'O que significa OVACE?', 
   'r1':'Obstrução de Vias Aérias por Corpos Estranos', 
   'r2':'Obstrução de Vias Aerobicas por Comportamentos Estranhos', 
   'r3':'Obstrução Visual Atrofica por Confecção Excêntrica', 
   'r4':'Obstrução Visual Anti-Corpotamental Escalonavel'
  },
  
  {
    'Pergunta':'Ao socorrer uma vitima de queimadura de 1° e 2° grau, o que é necessário fazer?', 
    'r1':'Cobrir as queimaduras com gase molhada em soro ou água fria, e trocando conforme for aquecendo.', 
    'r2':'Cobrir as queimaduras com gase molhada em soro ou água quente, e trocando conforme for esfriando.', 
    'r3':'Esfregar até que a pele morta saia, e estourar todas as bolhas', 
    'r4':'Passar pasta de dente'
  },
  
  {
    'Pergunta':'Qual manobra é utilizada para desengasgar uma pessoa?', 
    'r1':'Heimlich', 
    'r2':'FAB e FAF', 
    'r3':'Estancamento', 
    'r4':'RCP'
  },
  
  {
    'Pergunta':'Ao socorre uma vitima de FAB o que é essencial fazer?', 
    'r1':'Ligar para o socorro especializado, não remover o objeto cravado, fazer compressa e imobilização do objeto e manter a vitima deitada imovel.',
    'r2':'Remover o objeto cravado, e fazer estancamento, ligar para socorro especializado', 
    'r3':'Remover o objeto cravado e levantar a vitima e levala para o hospital mais proximo', 
    'r4':'Ligar para o socorro especializado e lateralizar a vitima.'
  },
  
  {
    'Pergunta':'Quando a um acedente de transito se a vitima for para em baixo do veico ou ficar presso em algum lugar para quem ligar?', 
    'r1':'193 - Corpo de Bombeiros', 
    'r2':'190 - Policia Militar', 
    'r3':'192 - SAMU', 
    'r4':'199 - Defesa Civil'
  },
  
  {
    'Pergunta':'Qual Norma Técnica fala sobre trabalho em altura?', 
    'r1':'NR35', 
    'r2':'NR20', 
    'r3':'NR16', 
    'r4':'NR28'
  },
  
  {
    'Pergunta':'Ao se deparar com um incêndio em equipamentos eletricos qual a melhor categoria de extintores a ser utilizada?', 
    'r1':'Categoria C (Extintor de CO²) ', 
    'r2':'Categoria A (Extintor de água)', 
    'r3':'Categoria B (Extintor de pó quimico)', 
    'r4':'Categoria D (Extintor de pó especifico para cada tipo de materiais)'
  },
]

print('\n' + theme);

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
