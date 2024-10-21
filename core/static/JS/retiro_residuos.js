

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

function mapa(){
    let coordenadas = {lat: -33.6942128, lng: -71.2136897}
    let map = new google.maps.Map(document.querySelector("#map"),
    {
        zoom: 20,
        center: coordenadas
    })
    var marker = new google.maps.Marker({
    position: coordenadas,
    map: map
  });
}