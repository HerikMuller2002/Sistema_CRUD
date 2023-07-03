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
document.addEventListener('DOMContentLoaded', function() {
  get_list_names();
});



// função para criar elemento tabela no HTML
function create_table_div(tabela, divId) {
  var div = document.getElementById(divId);
  var table = document.createElement('table');
  table.className = 'table';
  table.setAttribute('id', "table");
  var thead = document.createElement('thead');
  var headerRow = document.createElement('tr');
  var columns = tabela[0];
  for (var i = 0; i < columns.length; i++) {
    var columnName = columns[i];
    var th = document.createElement('th');
    th.setAttribute('scope', 'col');
    th.textContent = columnName;
    headerRow.appendChild(th);
  }
  thead.appendChild(headerRow);
  table.appendChild(thead);
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



function disabledFilter(){
  var select_db = document.getElementById('dropdown_database');
  var select_table = document.getElementById('dropdown_tables');
  var select_db_Value = select_db.value;
  if (select_db_Value){
    select_table.disabled = false;
  }
}


// função para verificar select
function displaySelectedTable() {
  var divId = 'main-content-bottom';
  var select_table = document.getElementById('dropdown_tables');
  var select_db = document.getElementById('dropdown_database');
  var select_db_Value = select_db.value;
  var select_table_Value = select_table.value;
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
      selected_line();

      button_add.disabled = false;
      button_download.disabled = false;

      if (selectedRow && selectedRow.parentNode === table) {
        button_edit.disabled = false;
        button_delete.disabled = false;
      } else {
        button_edit.disabled = true;
        button_delete.disabled = true;
      }
    })
    .catch(function(error) {
      console.error('Erro na requisição:', error);
    });
  }
}


// Adicione um identificador único para cada linha da tabela
var selectedRow = null;
var button_edit = document.getElementById("edit");
var button_delete = document.getElementById("delete");
var button_add = document.getElementById("add");
var button_download = document.getElementById("btn-export");

function selected_line(){
  var table = document.getElementById("table");
  var rows = table.getElementsByTagName("tr");
  for (var i = 0; i < rows.length; i++) {
    rows[i].onclick = function() {
      if (event.target.tagName.toLowerCase() === "th") {
        return;
      }
      var current = document.getElementsByClassName("selected");
      if (current.length > 0) {
        current[0].className = current[0].className.replace(" selected", "");
      }
      this.className += " selected";
      selectedRow = this;
      button_edit.disabled = false;
      button_delete.disabled = false;
    };
  }
}



// função para filtrar tabela
function filterTable() {
  var searchBar = document.getElementById("search-bar");
  var table = document.getElementById("table");
  var rows = table.getElementsByTagName("tr");
  var filter = searchBar.value.toLowerCase();
  for (var i = 1; i < rows.length; i++) {
      var cells = rows[i].getElementsByTagName("td");
      var display = false;
      for (var j = 0; j < cells.length; j++) {
          if (cells[j].innerHTML.toLowerCase().indexOf(filter) > -1) {
              display = true;
              break;
          }
      }
      if (display) {
          rows[i].style.display = "";
      } else {
          rows[i].style.display = "none";
      }
  }
}


// Download da tabela
function exportToExcel() {
  const table = document.getElementById('table');
  const ws = XLSX.utils.table_to_sheet(table);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, 'Tabela');
  const currentDate = new Date();
  const filename = 'tabela_' + currentDate.toISOString() + '.xlsx';
  const wbout = XLSX.write(wb, { bookType: 'xlsx', type: 'array' });
  const blob = new Blob([wbout], { type: 'application/octet-stream' });
  if (typeof navigator.msSaveBlob !== 'undefined') {
    navigator.msSaveBlob(blob, filename);
  } else {
    const link = document.createElement('a');
    if (link.download !== undefined) {
      const url = URL.createObjectURL(blob);
      link.setAttribute('href', url);
      link.setAttribute('download', filename);
      link.style.visibility = 'hidden';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  }
}
const downloadBtn = document.getElementById('btn-export');
downloadBtn.addEventListener('click', exportToExcel);



// Função para abrir o modal
function openModal(button) {
  var buttonId = button.id;
  console.log(buttonId)
  
  var modal = document.getElementById('modal-crud-add');
  modal.style.display = 'flex';
}

// Função para fechar o modal
function closeModal() {
  var modal = document.getElementById('modal-crud-add');
  modal.style.display = 'none';
}