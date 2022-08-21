var formLogin=document.getElementById('formLogin') //obteniendo el formulario

/* vamos a escuchas cuando se realice el evento ON SUBMIT*/
formLogin.onsubmit=function(event){
    event.preventDefault(); /*previene el comportamiento por default de mi formulario*/

    //creamos una variable con todos los datos del formulario
    var formulario=new FormData(formLogin);
    /*
    formulario={
        "email":"elena@codingdojo.com"
        "password":"1234"
    }
    */
    fetch("/login", {method:'POST', body:formulario})
    .then(response=> response.json())
    .then(data=>{
        console.log(data);

        if (data.message=="correcto"){
            window.location.href="/dashboard"
        }
        var mensajeAlerta=document.getElementById('mensajeAlerta'); //
        mensajeAlerta.innerText=data.message;
        mensajeAlerta.classList.add('alert');
        mensajeAlerta.classList.add('alert-danger')
    });
    /*
    function x(data){
        console.lo(data);
    }
    */
}

