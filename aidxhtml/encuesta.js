function isNumberKey(evt) {
    const charCode = (evt.which) ? evt.which : evt.keyCode;
    return !(charCode > 31 && (charCode < 48 || charCode > 57));
}

function preventNonNumericPaste(evt) {
    const pastedText = evt.clipboardData.getData('text');
    if (!/^\d+$/.test(pastedText)) {
        evt.preventDefault();
        return false;
    }
    return true;
}


function validateForm() {
    var conocimiento = document.forms[0]["conocimiento"].value;
    var experiencia = document.forms[0]["experiencia"].value;
    var comentario = document.forms[0]["comentario"].value;
    var tipo_archivos = document.forms[0]["tipo_archivos"].value;
    var respaldo = document.forms[0]["respaldo"].value;
    var victima_previa = document.forms[0]["victima_previa"].value;
    var plan_alternativo = document.forms[0]["plan_alternativo"].value;
    var notificacion_ransomware = document.forms[0]["notificacion_ransomware"].value;

    // Verifica que todos los campos estén completos
    if (conocimiento && experiencia && comentario && tipo_archivos && respaldo && victima_previa && plan_alternativo && notificacion_ransomware) {
        document.getElementById("submitBtn").removeAttribute("disabled"); // Habilita el botón de envío
        return true; // Envía el formulario si todo está completo
    } else {
        alert("Por favor, complete todas las respuestas antes de enviar.");
        return false; // Evita el envío del formulario si faltan respuestas
    }
}


if (formularioEsValido) {
    window.location.href = "descargaprogramadescriptadoxd.html";
    return false; // Esto evitará que el formulario se envíe al servidor
}


    // JavaScript para habilitar el botón de envío cuando se completa el formulario
    document.addEventListener("DOMContentLoaded", function () {
        const encuestaForm = document.getElementById("encuestaForm");
        const submitBtn = document.getElementById("submitBtn");

        encuestaForm.addEventListener("change", function () {
            // Verificar si todos los campos obligatorios están completos
            const allFieldsValid = Array.from(encuestaForm.elements).every(function (element) {
                return element.checkValidity();
            });

            // Habilitar o deshabilitar el botón de envío según el estado de los campos
            submitBtn.disabled = !allFieldsValid;
        });
    });