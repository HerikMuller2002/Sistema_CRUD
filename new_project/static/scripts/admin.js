// Servidor flask
const url_get_list_names = 'http://localhost:5050'



$(document).ready(function() {
    $('.js-example-matcher-start').select2();
});



// função para deitar string (capitalize)
function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}



// Dropdown Filter database
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
  


// Dropdown Filter tables
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



// função para pegar o nomes dos db e tabelas
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
// executa essa função quando a pagina é carregada
document.addEventListener('DOMContentLoaded', get_list_names);



// função para criar elemento tabela no HTML
function create_table_div(tabela, divId) {
  var div = document.getElementById(divId);
  var table = document.createElement('table');
  table.className = 'table';
  table.setAttribute('id', "table");
  var thead = document.createElement('thead');
  var headerRow = document.createElement('tr');
  var columns = tabela[0]; // Obtém a primeira tupla como os nomes das colunas
  for (var i = 0; i < columns.length; i++) {
    var columnName = columns[i];
    var th = document.createElement('th');
    th.setAttribute('scope', 'col');
    th.textContent = columnName;
    headerRow.appendChild(th);
  }
  thead.appendChild(headerRow);
  table.appendChild(thead);

  // Verifica se há linhas de dados além do cabeçalho
  if (tabela.length > 1) {
    var tbody = document.createElement('tbody');
    for (var rowIndex = 1; rowIndex < tabela.length; rowIndex++) {
      var rowData = tabela[rowIndex];
      var row = document.createElement('tr');
      for (var colIndex = 0; colIndex < columns.length; colIndex++) {
        var cellValue = rowData[colIndex];
        var td = document.createElement('td');
        td.textContent = cellValue;
        row.appendChild(td);
      }
      tbody.appendChild(row);
    }
    table.appendChild(tbody);
  }

  div.innerHTML = '';
  div.appendChild(table);
}




// função para verificar select
function displaySelectedTable() {
  var select_db = document.getElementById('dropdown_database');
  var select_table = document.getElementById('dropdown_tables');
  var divId = 'main-content-bottom';
  var select_table_Value = select_table.value;
  var select_db_Value = select_db.value;
  if (select_table_Value && select_db_Value) {
    var data = {
      'database_name': select_db_Value,
      'table_name': select_table_Value
    };
    fetch('/get_table', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(function(response) {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Erro na requisição: ' + response.status);
      }
    })
    .then(function(data) {
      create_table_div(data, divId);
    })
    .catch(function(error) {
      console.error('Erro na requisição:', error);
    });
  }
}
