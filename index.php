<!DOCTYPE html>
<html lang="en">

<head>
  <?php
  header("Cache-Control: no-cache, must-revalidate"); // HTTP/1.1
  header("Expires: Sat, 1 Jul 2000 05:00:00 GMT"); // Fecha en el pasado
  ?>
  <!--limpiar cache-->
  <meta http-equiv=”Expires” content=”0″>
  <meta http-equiv=”Last-Modified” content=”0″>
  <meta http-equiv=”Cache-Control” content=”no-cache, mustrevalidate”>
  <meta http-equiv=”Pragma” content=”no-cache”>
  <!--html-->
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TALLER MECANICO RAYO MCQUEEN</title>
  <link rel="website icon" type="png" href="imagen/rasho.png">
  <!--css-->
  <link rel="stylesheet" type="text/css" href="CSS/footer.css?1.0" media="all" ">
  <link rel=" stylesheet" type="text/css" href="CSS/trabajos.css?1.0" media="all" ">
  <link rel=" stylesheet" type="text/css" href="CSS/formulario.css?1.0" media="all" ">
  <link rel=" stylesheet" type="text/css" href="CSS/parrafos.css">
  <!--bootstrap-->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
  <!--cloudfare-->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />
  <!--jquery-->
  <script src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
  <!--sweetalert-->
  <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
  <script src="sweetalert2.all.min.js"></script>
  <!--llamar al nav-->
  <script>
    $(function nav() {
      $("#includeHtml").load("nav.html");
    });
  </script>
</head>

<body>
  <!--incluir nav-->
  <div id="includeHtml" style="position: relative; z-index: 2;"></div>
  <!--carrusel-->
  <div class="CONTENEDOR" style="width: auto; height: auto; z-index: 1;">
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <h5 class="animate__animated animate__bounceOutRight" style="font-size: 5em; margin-left: 30%; color: red;">
            ¡¡¡Bienvenidos!!!</h5>
          <img src="imagen/rasho.png" class="d-block w-100" alt="10">
          <div class="carousel-caption d-none d-md-block">
            <h5 class="parrafo-frenos">Trabajos</h5>
            <p class="parrafo-frenos">Aquí podra ver algunos trabajos realizados</p>
            <div class="card-link">
              <a class="link" href="frenos.html">
                <p class="box">
                  <p class="parrafo-especial">Ver más</p>
                </p>
              </a>
            </div>
          </div>
        </div>
        <div class="carousel-item">
          <img src="imagen/mecanico-automoviles-cambiando-ruedas-coche.jpg" class="d-block w-100" alt="10">
          <div class="carousel-caption d-none d-md-block">
            <h5 class="parrafo-frenos">Mecánicos</h5>
            <p class="parrafo-frenos">Aqui podra ver el equipo como trabaja</p>
            <div class="card-link">
              <a class="link" href="ba.html">
                <p class="box">
                  <p class="parrafo-especial">Ver mas</p>
                </p>
              </a>
            </div>
          </div>
        </div>
        <div class="carousel-item">
          <img src="imagen/trabajador-servicio-coche-musculoso-reparando-vehiculo.jpg" class="d-block w-100" alt="10">
          <div class="carousel-caption d-none d-md-block">
            <h5 class="parrafo-frenos">Revision tecnica</h5>
            <p class="parrafo-frenos">¡¡¡¡conoce como trabajamos!!!!</p>
            <div class="card-link">
              <a class="link" href="pulido.html">
                <p class="box">
                  <p class="parrafo-especial">Ver mas</p>
                </p>
              </a>
            </div>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
  <!--footer-->
  <footer class="footer">
    <h3 style="font-style: italic; color: crimson;">¡Encuentranos en!</h3>
    <div class="button">
      <div class="top-social">
        <ul>
          <li><a href="https://es-la.facebook.com/" class="facebook"><i class="fa fa-facebook-f fa-2x"></i></a></li>
          <li><a href="https://www.instagram.com/" class="instagram"><i class="fa fa-instagram fa-2x"></i></a></li>
          <li><a href="https://twitter.com/" class="twitter"><i class="fa fa-twitter fa-2x"></i></a></li>
          <li><a href="https://www.youtube.com/" class="youtube"><i class="fa fa-youtube fa-2x"></i></a></li>
        </ul>
        <p style="font-style: italic; color: crimson; font-size: 20px;">Te esperamos en nuestra Sucursal av.cuchau 95
          cerca de la ruta 66😉</p>
        <p style="font-style: italic; color: crimson; font-size: 20px;">horario de atención de lunes a jueves 08:30 -
          18:30</p>
        <p style="font-style: italic; color: crimson; font-size: 20px;">y viernes de 08:30 - 17:30</p>
      </div>
    </div>
    <form class="formail" action="mail.php" method="post">
      <h2>Contacto</h2>
      <div class="formail-group">
        <label for="name">Nombre</label>
        <input type="text" id="name" name="name" placeholder="nombre y apellido" required>
      </div>
      <div class="formail-group">
        <label for="teléfono">telefono</label>
        <input type="text" id="telefono" name="fono" placeholder="+56912345678" required>
      </div>
      <div class="formail-group">
        <label for="email">Correo electrónico</label>
        <input type="email" id="email" name="email" placeholder="example@gmail.com" required>
      </div>
      <button class="boton-formail" type="submit" name="enviar">enviar solicitud</button>
    </form>
  </footer>
  <?php
  if (isset($_REQUEST['confirmado'])) {
  ?>
    <script>
      Swal.fire({
        title: 'datos enviados',
        text: 'le contactaremos a la brevedad',
        confirmButtonText: 'aceptar'
      })
    </script>
  <?php }
  ?>
  <!--IMPORTACIONES-->
  <!--  JS JQUERY -->
  <script src="assets/js/jquery/jquery-3.6.4.min.js"></script>
  <script src="assets/js/jquery/jquery-ui.js"></script>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
  <!--BOOSTRAP -->
  <script src="assets/js/bootstrap/bootstrap.bundle.min.js"></script>
  <!--JS DE PERSONALIZADO -->
  <script src="assets/js/app.js"></script>
</body>

</html>