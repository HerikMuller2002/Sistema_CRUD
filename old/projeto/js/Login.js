function login(email_key="admin", password_key="123") {
    var email = document.getElementById("inputEmail").value;
    var password = document.getElementById("inputPassword").value;

    if (email == email_key && password == password_key) {
        alert("Login feito com sucesso!")
        location.href = "index.html"
    } else {
        alert("Email e senha incorretos!")
        var inputPassword = document.getElementById("inputPassword");
        var errorDiv = document.getElementById("password-error");
        inputPassword.classList.add("is-invalid");
        errorDiv.innerHTML = "Senha incorreta";
        errorDiv.style.display = "block";
    }
};
