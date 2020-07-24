// Captura de datos desde el HTML 
let nombre          = document.getElementById('nombre').value;
let apellido        = document.getElementById('apellido').value;
let numDoc          = document.getElementById('num-doc').value;
let edad            = document.getElementById('edad').value;
let telefono        = document.getElementById('telefono').value;
let email           = document.getElementById('email').value;
let fechaConsulta   = document.getElementById('fecha-consulta').value;
let horaConsulta    = document.getElementById('hora-consulta').value;
let motivo          = document.getElementById('motivo').value;

/**
 * Agrupa los valores de los campos de texto del HTML
 * en un objeto JSON
 */
function clickButton() {

    const consulta = {
        nombre,
        apellido,
        numDoc,
        edad,
        telefono,
        email,
        fechaConsulta,
        horaConsulta,
        motivo,
    }
    enviarAlServidor(consulta)
}

/**
 * RESTFUL
 * Envia los datos a nuestro servidor
 */
function enviarAlServidor(dataAEnviar) {
    axios({
        method  : 'POST', // REQUEST
        url     : "http://localhost:5000/agendar-cita",
        data    : dataAEnviar
    })
    .then( (respuesta) => { // RESPONSE
        alert(respuesta.data.mensaje)
    })
}