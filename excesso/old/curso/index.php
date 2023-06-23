<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <title>Formulário</title>
        <link rel="stylesheet" href="css/bootstrap.css">

        <style type="text/css">
            #tamanhoContainer {
                width: 500px;
            }
        </style>

    </head>
    <body>
        <script type="text/javascript" src="js/bootstrap.js"></script>

        <div class="container" id="tamanhoContainer" style="margin-top: 40px">
            <h3>Formulário</h3>
            <form style="margin-top: 20px;">
                <div class="form-group">
                    <label>Nro Produto</label>
                    <input type="number" class="form-control" placeholder="Insira o número do produto">
                </div>
                <div class="form-group">
                    <label>Nome Produto</label>
                    <input type="text" class="form-control" placeholder="Insira o nome do produto">
                </div>
                <div class="form-group">
                    <label>Categoria</label>
                    <select class="form-select">
                        <option>Periféricos</option>
                        <option>Hardware</option>
                        <option>Software</option>
                        <option>Celulares</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Quantidade</label>
                    <input type="number" class="form-control" placeholder="Insira a quantidade">
                </div>
                <div class="form-group">
                    <label>Fornecedor</label>
                    <select class="form-select">
                        <option>Fornecedor A</option>
                        <option>Fornecedor B</option>
                        <option>Fornecedor C</option>
                        <option>Fornecedor D</option>
                    </select>
                </div>
                <div style="text-align: right;">
                    <button type="submit" class="btn btn-outline-success">Cadastrar</button>
                </div>
            </form>
        </div>
        
    </body>
    </html>