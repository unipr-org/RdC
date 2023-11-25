<html>

<head>      
<title>PHP: Variabili superglobali </title>
session_start();
</head>

 <body>

  <a href="<?php echo "http://".$_SERVER['HTTP_HOST'].$_SERVER['PHP_SELF']?>"> home </a>
          
  <br> <font color="red">foreach $_SERVER </font>
  <br> <?php  foreach ($_SERVER as $param => $val)  echo "$param: $val<br>"; ?>

  <br> <font color="red">foreach $_GET </font>
  <br><?php  foreach ($_GET as $param => $val)  echo "$param: $val<br>"; ?>

  <br> <font color="red">foreach $_POST </font>
  <br><?php  foreach ($_POST as $param => $val)  echo "$param: $val<br>"; ?>

  <br> <font color="red">foreach $_COOKIE </font>
  <br><?php  foreach ($_COOKIE as $param => $val)  echo "$param: $val<br>"; ?>
  
  <br> <font color="red">foreach $_REQUEST (GET+POST+COOKIE) </font>   
  <br><?php  foreach ($_REQUEST as $param => $val)  echo "$param: $val<br>"; ?>

  <br> <font color="red">foreach $_ENV </font>
  <br><?php  foreach ($_ENV as $param => $val)  echo "$param: $val<br>"; ?>

  <br> <font color="red">foreach $_SESSION </font>
  <br><?php  foreach ($_SESSION as $param => $val)  echo "$param: $val<br>"; ?>

  <hr/>

 </body>

</html>

