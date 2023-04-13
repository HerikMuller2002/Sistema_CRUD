<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <title>Chat Bot system</title>
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <script type="text/javascript" src="js/bootstrap.js"></script>
    <div id="page-content" style="height: 100%;">
        <div id="login">
            <div id="login-form">
                <div id="login-logo">
                    <img id="login-logo-img" src="../assets/logo-semeq-branco.png">
                </div>
                <div id="login-box">
                    <div id="login-title">
                        <h1 id="login-title-text">Sistema de Gerenciamento</h1>
                    </div>
                    <div id="login-error" class="login-error">
                        <div id="login-error-text" class="login-error-text">Usuário ou senha incorretos</div>
                    </div>
                    <div id="login-inputs" class="login-inputs">
                        <input type="text" placeholder="Usuário" class="input" id="login-input-user" step="any" persisted_props="value" persistence_type="local" value="">
                        <input type="password" placeholder="Senha" class="input" id="login-input-password" step="any" persisted_props="value" persistence_type="local" value="">
                        <button id="login-button" class="btn">Login</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>