function validarContrasenia(){
    let user = document.querySelector("#contrasenia");
    if(user.value == "hola"){
        user.classList.add("correct");
        user.classList.remove("incorrect");
    }else{
        user.classList.add("incorrect");
        user.classList.remove("correct");
    }
}