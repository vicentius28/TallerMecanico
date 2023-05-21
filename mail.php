<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';
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
?>
    <script>
        Swal.fire({
            title: 'datos enviados',
            text: 'le contactaremos a la brevedad',
            confirmButtonText: 'aceptar'
        })
    </script>
<?php }
$str = 'nombre: ' . $nombre;
$str .= 'telefono: ' . $fono;
$str .= 'correo: ' . $correo;

try {
    //Server settings
    $mail->SMTPDebug = SMTP::DEBUG_SERVER;                      //Enable verbose debug output
    $mail->isSMTP();                                            //Send using SMTP
    $mail->Host       = 'smtp@gmail.com';                     //Set the SMTP server to send through
    $mail->SMTPAuth   = true;
    $email = 'vicente.farias2812@gmail.com';        //Enable SMTP authentication
    $mail->Username   = $email;                  //SMTP username
    $mail->Password   = 'tfuvlkefgqqbxfjh';                               //SMTP password
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;            //Enable implicit TLS encryption
    $mail->Port       = 465;                                    //TCP port to connect to; use 587 if you have set `SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS`

    //Recipients
    $mail->setFrom($email, $nombre);
    $mail->addCC($correo);  //Add a recipient



    //Attachments
    $mail->addAttachment('/var/tmp/file.tar.gz');         //Add attachments
    $mail->addAttachment('/tmp/image.jpg', 'new.jpg');    //Optional name

    //Content
    $mail->isHTML(true);                                  //Set email format to HTML
    $mail->Subject = 'Solicitud de contacto';
    $mail->Body    = $str;
    $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';
    header("refresh:4; url:caso.html");
    if (!$mail->send()) {
        throw new Exception($mail->ErrorInfo);
    }
} catch (Exception $e) {
    echo ("ERROR");
}
