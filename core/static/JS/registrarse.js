function capitalize(texto){
    let palabras = "";
    if(typeof texto === "string" && texto.trim().length > 0){
        for (const iterator of texto.split(" ")) {
            //console.log(iterator[0].toUpperCase());
            for (const letra in iterator){
                if (letra == 0){
                    palabras += iterator[letra].toUpperCase();
                }else{
                    palabras += iterator[letra].toLowerCase();
                }
            }
            palabras += " ";
        }
        return palabras.trim();
    }else{
        return;
    }
}




function validarCreacionCuenta(){
    let user = document.querySelector("#id_username");
    let email = document.querySelector("#id_email");
    let pass  = document.querySelector("#id_password1");
    let pass2 = document.querySelector("#id_password2");

    if (user.value.trim() == "" || email.value.trim() == "" || pass.value.trim() == "" || pass2.value.trim() == ""){
        document.querySelector("#error-user").innerHTML = "Ingrese un nombre de usuario"
        document.querySelector("#error-email").innerHTML = "Ingrese un email"
        document.querySelector("#error-password1").innerHTML = "Ingrese una contraseña"
    }else{
        if (pass.value == pass2.value){
            document.querySelector("#error-password2").innerHTML = "Las contraseñas no son iguales"
        }
    }
}