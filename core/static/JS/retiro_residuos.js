

function mostrarMensaje(){
    alert("Debes iniciar sesión primero")
}

function validarCant(){
    if (document.querySelector("#id_cant_residuos").value > 2){
        document.querySelector("#mayor").setAttribute("style", "display: block;")
        document.querySelector("#menor").setAttribute("style", "display: none;")
    }else{
        document.querySelector("#mayor").setAttribute("style", "display: none;")
        document.querySelector("#menor").setAttribute("style", "display: block;")
    }

    if (document.querySelector("#id_cant_residuos").value <= 0){
        document.querySelector("#id_cant_residuos").value = 1
    }
}

function pasarelaPago(){
    document.getElementById("formulario-residuo").submit();
    window.location.href = '../pago/';
}