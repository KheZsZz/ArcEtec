 //Recebe todos os dados do aquivo json

// 1) Criar uma função que irá realizar a leitura do arquivo JSON para receber as informações e poder retornar os dados numa variável que for necessário.
const allData= async () => {
  const data = require ('./estados-cidades-atividade.json');
  return data;
}

// 2) Criar uma função que liste o nome de todos os estados salvos no arquivo.
const listAllState = async () => {
  const data = await allData();
  data.map(item=>console.log(item.nome))
}
listAllState();

//3) Criar uma função que liste o nome de todos os estados inciados com a letra A salvos no arquivo.
const listAllStatePLetra = async (letra) =>{
  const data = await allData();
  data.map((item) => {
    item.nome.substring(0,1) === letra ? console.log(item.nome) : null
  })
}
listAllStatePLetra("A");

// 4) Criar uma função que liste todos os nomes dos estados ordenados primeiramente por qual estado tem menos letras.
const listOrderBy = async () => {
  const data = await allData();
  data.sort((a, b) => a.nome.length - b.nome.length);
  data.map((item) =>{console.log(item.nome)})
}
listOrderBy();

//5. Criar uma função que liste os nomes de todas as cidades do estado de São Paulo.
const citys = async (estado) => {
  const data = await allData();
  data.forEach((item)=>{item.nome === estado ? console.log(item.cidades): null})
}
citys("São Paulo");

//6. Criar uma função que liste o nome de todas as cidades do Maranhão com mais de 6 letras.
const citysMaior = async (state, maior) => {
  const data = await allData();
  data.map((item) => {
    if (item.nome == state) { item.cidades.map((city) => {
        city.length > maior ? console.log(city):null
      });
    }
  });
}
citysMaior("Maranhão", 6)

//7. Criar uma função que informe o nome dos estados e quantas cidades cada um deles posui.
const stateTotalCity = async () => {
  const data = await allData();
  console.table(data.map(item=>[item.nome, item.cidades.length]))
}
stateTotalCity();

//8. Criar uma função que liste o nome de todas as cidades da Bahia com menos de 5 letras.
const citysMenor = async (state, menor) => {
  const data = await allData();
  data.map((item) => {
    if (item.nome == state) { item.cidades.map((city) => {
        city.length < menor ? console.log(city):null
      });
    }
  });
}
citysMenor("Bahia", 5)