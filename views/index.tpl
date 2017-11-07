<!DOCTYPE html>
<html > 
<head>
  <meta charset="UTF-8">
  <title>Formulario</title>
      <link rel="stylesheet" href="/views/css/style.css">
</head>
<body>
  <div class="login-page">
  <div class="form">
    <form class="login-form" action="acceso" method="post">
      <input type="text" placeholder="username" name="username"/>
      <input type="password" placeholder="password" name="password"/>
      <input type="text" placeholder="host" name="host"/>
      <input type="text" placeholder="basedatos" name="basedatos"/>
      <div class="submit-container">
      <input type="submit" value="login"/>
      </div>
    </form>
  </div>
</div>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
    <script  src="js/index.js"></script>
</body>
</html>