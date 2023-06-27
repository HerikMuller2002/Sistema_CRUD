const url_get_list_names = 'http://localhost:5050'

$(document).ready(function() {
    $('.js-example-matcher-start').select2();
});

function get_list_names() {
    event.preventDefault();
    
    fetch(url_get_list_names + '/get_list_names')
      .then(response => response.json())
      .then(data => {

        console.log(data);

      })
      .catch(error => {
        console.error('Erro ao obter bancos de dados:', error);
      });
  }

var botao = document.getElementById("add");
botao.addEventListener("click", get_list_names);