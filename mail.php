<?php
ob_start();

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

//Load Composer's autoloader
require 'vendor/autoload.php';
echo <<< HTML
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
<script src="sweetalert2.all.min.js"></script>
HTML;


$mail = new PHPMailer(true);

if (isset($_POST['enviar'])) {
    if (!empty($_POST['name']) && !empty($_POST['fono']) && !empty($_POST['email'])) {
        $nombre = ($_POST['name']);
        $fono = ($_POST['fono']);
        $correo = ($_POST['email']);
    }
}
$str = "<div style=\"width: 90vh;
            height: 40vh;
            margin-left: 10%;
            margin-top: 3%;
            background-color: gray;
            border-color: #4a4a4a;
            color: black;
            max-width: 100%;
            position: relative;
            padding: 2%;\"> 
            <div style=\"position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);\">
                <h1>Contacto</h1>
            <div style=\"width: 500px;
                height: 60px;
                background-color: white;
                border-color: gray;
                border-width: 1px;
                border-style: solid;
                position: relative;
                padding-left: 10px;\">
                <p> <strong>Nombre:</strong> $nombre</p>
            </div>
            <div style=\"width: 500px;
                height: 60px;
                background-color: #fff;
                border-color: gray;
                border-width: 1px;
                border-style: solid;
                position: relative;
                padding-left: 10px;\">
                <p>telefono: $fono</p>
            </div>
            <div style=\"width: 500px;
                height: 60px;
                background-color: #fff;
                border-color: gray;
                border-width: 1px;
                border-style: solid;
                position: relative;
                padding-left: 10px;\">
                <p>correo: $correo</p>
            </div>
        </div>
    </div>";
header("Location: index.php?confirmado=1");
try {
    $mail = new PHPMailer(true);
    //Server settings
    $mail->SMTPDebug = SMTP::DEBUG_SERVER;                      //Enable verbose debug output
    $mail->isSMTP();                                            //Send using SMTP
    $mail->Host = 'smtp.gmail.com';                //Set the SMTP server to send through
    $mail->SMTPAuth   = true;
    $email = 'vicente.farias2812@gmail.com';        //Enable SMTP authentication
    $mail->Username   = $email;                  //SMTP username
    $mail->Password   = 'tfuvlkefgqqbxfjh';                               //SMTP password
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;            //Enable implicit TLS encryption
    $mail->Port       = 465;                                    //TCP port to connect to; use 587 if you have set `SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS`

    // Quien envía este mensaje
    $mail->setFrom($email, $nombre);

    // Destinatario
    $mail->addAddress('vic.fariasm@duocuc.cl');
    $mail->addCC($correo);

    //Content
    $mail->IsHTML(true);
    $mail->CharSet = 'UTF-8';                                 //Set email format to HTML
    $mail->Subject = 'Solicitud de contacto';
    $mail->Body    = $str;
    if (!$mail->send()) {
        throw new Exception($mail->ErrorInfo);
    }
} catch (Exception $e) {
    header("refresh:3;url=index.php");
?>
    <script>
        Swal.fire({
            title: 'Error!',
            text: 'ingrese un correo valido',
            icon: 'error',
            confirmButtonText: 'aceptar'
        })
    </script>
<?php
}
