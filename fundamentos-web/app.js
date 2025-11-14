console.log("JavaScript carregado!");

const botao = document.getElementById("meu-botao");
const titulo = document.getElementById("titulo-principal");
const nome = document.getElementById("caixa-nome")
const lista = document.getElementById("lista-de-tarefas")

botao.addEventListener("click", () => {
  /*const nomeDigitado = nome.value;*/
  const textoDaTarefa = nome.value;
  /*titulo.textContent = `Olá, ${nomeDigitado}`;*/
  const novoItem = document.createElement("li");
  novoItem.textContent = textoDaTarefa
  lista.appendChild(novoItem)
  nome.value = '';
  /*console.log("O botão foi clicado!");*/
});

lista.addEventListener("click", () => {
  if (event.target.tagName === 'LI'){
    event.target.remove();
  }
});

nome.addEventListener("keydown", (event) => {
  if (event.key === "Enter"){
    botao.click()
  }
})