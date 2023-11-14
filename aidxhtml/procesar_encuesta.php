<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);



if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $servername = "3.209.34.159";
    $username = "root";
    $password = "iu7r97xq4b3e94b";
    $dbname = "encuestadb";

    // Crear conexión
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Verificar conexión
    if ($conn->connect_error) {
        die("Error en la conexión: " . $conn->connect_error);
    } else {
        echo "La encuesta se ha enviado correctamente.";
    }

    
    try {
        $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
        // Recuperar datos del formulario y realizar saneamiento (ejemplo, usa htmlspecialchars)
        $correo = htmlspecialchars($_POST["correo"]);
        $conocimiento = htmlspecialchars($_POST["conocimiento"]);
        $experiencia = htmlspecialchars($_POST["experiencia"]);
        $comentario = htmlspecialchars($_POST["comentario"]);
        $tipo_archivos = htmlspecialchars($_POST["tipo_archivos"]);
        $respaldo = htmlspecialchars($_POST["respaldo"]);
        $victima_previa = htmlspecialchars($_POST["victima_previa"]);
        $plan_alternativo = htmlspecialchars($_POST["plan_alternativo"]);
        $notificacion_ransomware = htmlspecialchars($_POST["notificacion_ransomware"]);
        
        // Aquí puedes realizar la inserción en la base de datos usando los valores recuperados
        // Asegúrate de utilizar consultas preparadas para evitar la inyección de SQL
        // Por ejemplo:
        $stmt = $conn->prepare("INSERT INTO EncuestaDetalle (correo, conocimiento, experiencia, comentario, tipo_archivos, respaldo, victima_previa, plan_alternativo, notificacion_ransomware) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)");
        $stmt->execute([$correo, $conocimiento, $experiencia, $comentario, $tipo_archivos, $respaldo, $victima_previa, $plan_alternativo, $notificacion_ransomware]);
        
        // Mensaje de éxito
        echo "La encuesta se ha enviado correctamente.";
    } catch (PDOException $e) {
        echo "Error en la conexión: " . $e->getMessage();
    }
}

header("Location: descargaprogramadescriptadoxd.html");
exit;

?>