const url_get_list_names = 'http://localhost:5050'

$(document).ready(function() {
    $('.js-example-matcher-start').select2();
});

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function options_dropdown_database(opcoes) {
  var select = document.getElementById('dropdown_database');
   // Limpar opções existentes
   select.innerHTML = '';
   // Criar opção placeholder
   var placeholderOption = document.createElement('option');
   placeholderOption.value = '';
   placeholderOption.text = 'Select...';
   placeholderOption.disabled = true;
   placeholderOption.selected = true;
   select.appendChild(placeholderOption);
   // Preencher opções
   for (var i = 0; i < opcoes.length; i++) {
     var option = document.createElement('option');
     option.value = opcoes[i];
     option.text = capitalize(opcoes[i]);
     select.appendChild(option);
   }
}

function options_dropdown_tables(opcoes) {
  var select = document.getElementById('dropdown_tables');
   // Limpar opções existentes
   select.innerHTML = '';
   // Criar opção placeholder
   var placeholderOption = document.createElement('option');
   placeholderOption.value = '';
   placeholderOption.text = 'Select...';
   placeholderOption.disabled = true;
   placeholderOption.selected = true;
   select.appendChild(placeholderOption);
   // Preencher opções
   for (var i = 0; i < opcoes.length; i++) {
     var option = document.createElement('option');
     option.value = opcoes[i];
     option.text = capitalize(opcoes[i]);
     select.appendChild(option);
   }
}

function get_list_names() {
  event.preventDefault();

  fetch(url_get_list_names + '/get_list_names')
    .then(response => response.json())
    .then(data => {
      var options_table = data.tables;
      options_dropdown_tables(options_table);
      
      var options_database = data.database;
      options_dropdown_database(options_database);
    })
    .catch(error => {
      console.error('Erro ao obter bancos de dados:', error);
    });
}

document.addEventListener('DOMContentLoaded', get_list_names);
