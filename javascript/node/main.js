const data = require ('./estados-cidades-atividade.json'); //Recebe todos os dados do aquivo json


const ListAllStates = async () => {
    data.map(item => console.log(item.nome))
}

const listStates = async (letra) => {
  data.filter((item)=>{item.nome.IndexOf(letra)})
}

listStates('A')

// ListAllStates();