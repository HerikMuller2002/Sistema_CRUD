document.addEventListener("DOMContentLoaded", function() {
    var inputEmail = document.getElementById("inputEmail");
    var inputPassword = document.getElementById("inputPassword");
    var btnLogin = document.getElementById("btn-login");
  
    btnLogin.addEventListener("click", function(event) {
      event.preventDefault();
  
      var email = inputEmail.value;
      var password = inputPassword.value;
  
      if (email === "admin" && password === "123") {
        window.location.href = "/new_project/pages/admin.html";
      } else {
          inputEmail.style.border = '1px solid red';
          inputPassword.style.border = '1px solid red';
          setTimeout(function() {
            inputEmail.style.border = '';
            inputPassword.style.border = '';
          }, 1000);
      }
    });
  });
  