const divPrincipal = document.querySelector("#divPrincipal");
const divJogo = document.querySelector("#divJogo");
const btnJogar = document.querySelector("#btnJogar");

btnJogar.addEventListener('click', function(){
    divPrincipal.style.display = "none";
    divJogo.style.display = "block";
    var text = document.querySelector("#secreto").value;
    localStorage.setItem('valueText', text);
});

var btn2 = document.querySelector("#inputButton2");

let tamanho = localStorage.getItem('valueText').length;

btn2.addEventListener("click", function () {
    var paragrafo = document.querySelector("#viewSessionStorage");
    paragrafo.textContent =  localStorage.getItem('valueText');
    let tamanho = localStorage.getItem('valueText').length;
    
    function underline(tamanho) {
    tamanhopalavra = '';
    for(i = 0; i < tamanho; i++){
        tamanhopalavra += '_ ';
    }
    console.log(tamanhopalavra)
    return tamanhopalavra
    }   
    var tamanhosecreto = document.querySelector("#PalavraSecreta");
    tamanhosecreto.textContent = underline(tamanho);
})

var btnTentar = document.querySelector("#btnTentar")