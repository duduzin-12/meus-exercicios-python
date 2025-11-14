const formNovoAluno = document.getElementById("form-novo-aluno");
const inputNome = document.getElementById("nome-aluno");
const inputNota = document.getElementById("nota-aluno");
const listaElementos = document.getElementById("lista-de-alunos");

function buscarAlunos(){
  fetch('http://127.0.0.1:5000/api/alunos')
  .then(resposta => resposta.json())
  .then(dados_da_turma =>{
    listaElementos.innerHTML = "";
    for (let aluno of dados_da_turma){
      const item = document.createElement("li")
      item.textContent = `Nome: ${aluno.nome}, Nota: ${aluno.nota}`
      item.dataset.nome = aluno.nome;
      listaElementos.appendChild(item)
    }
  })
};

listaElementos.addEventListener("click", (event) => {
  if(event.target.tagName === 'LI'){
    const nomeParaDeletar = event.target.dataset.nome;
    event.target.remove(); 
    fetch(`http://127.0.0.1:5000/api/aluno/${nomeParaDeletar}`, {
      method: 'DELETE',
    })
    .then(resposta => resposta.json())
    .then(dados => {
      console.log("Resposta do servidor:", dados);
    });
  };
});

formNovoAluno.addEventListener("submit", (event) =>{
  event.preventDefault();

  const nome = inputNome.value;
  const nota = inputNota.value;

  const novoAluno = {
        nome: nome,
        nota: parseFloat(nota)
  };

  fetch('http://127.0.0.1:5000/api/aluno', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', 
        },
        body: JSON.stringify(novoAluno),
    })
    .then(resposta => resposta.json())
    .then(dados => {
        console.log("Resposta do servidor:", dados);

        inputNome.value = "";
        inputNota.value = "";

        buscarAlunos();
    });
});