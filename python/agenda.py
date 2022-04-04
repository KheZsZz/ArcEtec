print ("\033[1;34m" + 'Bem vindo a sua agênda telefoneica!!! \n') # print em cyan

agenda = [
  {'name':'Kevin Oliveira',   'phone':'(11) 9.9577-8573'},
  {'name':'Giuliana Alcinio', 'phone':'(11) 9.4948-6492'},
  {'name':'Isabella Alcinio', 'phone': ''},
  {'name':'Samuel Pereira',   'phone': ''},
  {'name':'Mauricio Fabiano', 'phone':'(11) 9.7376-1687'}
] # Contatos Iniciais

esc = 0 # Escolha Inicial

def findOne(value, campo): # Função para encontra algo na agenda
  for i in agenda:
      if i.get(campo).find(value) == 0:
        return {'name':i.get('name', 'Não encontrado'), 'phone':i.get('phone','Não encontrado')} 
      else:
        return {'name':'Não encontrado', 'phone':'Não encontrado'} 
      
def AlterOne(value, campo): # Função para alterar algo na tabela
   for i in agenda:
      if i.get('name').find(value) == 0:
        if(campo == 'name'):
          newName = input('Digite o novo nome: ')
          i.update({campo: newName})
        if(campo == 'phone'):
          newPhone = input('Digite o novo phone: ')
          i.update({campo: newPhone})
        
        print("\033[0;32m" + '\nAtualizado com sucesso! \n') # print em verde
  
while esc != 6: # programa fica em execução até que a escolha seja igual a 6 (fechar programa)
  print("\033[0;0m")  # reset de cores do console
  esc = int(input (
    '\n1- Listar todos na agênda; \n'
    '2- Buscar um contato (pelo nome) \n'
    '3- Adcionar um contato \n'
    '4- Alterar um contato \n'
    '5- Sair \n'
  )) # pega a escolha do usuario
  
  match esc: #verifica as opções
    case 1: # Lista Todos
      for item in agenda:
        print("\033[1;36m" +'name: ' + item.get('name') + ' / ' + 'phone: ' + item.get('phone')) #print em cyan
    case 2: # Encontra um contato
      value = input('Digite o nome que deseja procurar: ') # pega o valor procurado seja nome ou telefone
      contato = findOne(value, 'name')
      if contato == None: # verifica se o dado informado existe na lista de nomes
        contato = findOne(value, 'phone') # Caso não exista procura na lista de telefones
      if(contato.get('name') == 'Não encontrado'):
        print("\033[1;31m" +'\n' + 'name: ' + contato.get('name') + '\n' 'phone: ' + contato.get('phone') + '\n') # print em Vermelho
      else:
        print("\033[0;32m"+'\n' + 'name: ' + contato.get('name') + '\n' 'phone: ' + contato.get('phone') + '\n') # print em verde
    case 3: # Add contato
      name = input('Digite o nome: ')
      phone = input('Digite o phone: ')
      agenda.insert(1, {'name': name, 'phone':phone}) # insere no dicionário
      print("\033[0;32m" + '\nInserido com sucesso! \n') #print em verde
    case 4: # Altera um valor
      name = input('Digite o nome que deseja alterar: ')
      campo = input('Digite o campo que deseja alterar: ')
      AlterOne(name, campo)
    case 5: # sair
      exit()