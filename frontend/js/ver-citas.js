/**
 * Carga los datos desde nuestro servidor
 */
!(function cargarCitas(){
    axios({
        method  : 'GET',
        url     : 'http://localhost:5000/ver-citas'
    }).then((respuesta) => {

        // Añade los datos dentro de la tabla HTML
        document.getElementById('table-body').innerHTML = respuesta.data.map((cita, index) => {
            return `
            <tr>
                <th scope="row">${index + 1 }</th>
                <td>${cita[3]} ${ cita[4] }</td>
                <td>${cita[7]}</td>
                <td>${cita[8]}</td>
                <td>${cita[5]}</td>
                <td>${cita[6]}</td>
                <td>${cita[1]}</td>
                <td>${cita[9]}</td>
            </tr>
            `;
        });
    })
})() // Esta funcion se autoejecuta cuando se carga la pagina