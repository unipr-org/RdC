<?php

header ("Content-Type: text/html");
session_start();
if (!isset($_SESSION['user'])) $_SESSION['user']="anonymous";

$_SESSION['home']="http://".$_SERVER['HTTP_HOST'].$_SERVER['SCRIPT_NAME'];

$ora = date ("d M Y H:i:s");


echo "<HTML>";
echo "<BODY>";
echo "<a href=".$_SESSION['home'].">HOME</a>"; 
echo " - ";
echo "Client Address: ".$_SERVER["REMOTE_ADDR"];
echo " - ";
echo  "User Agent: ".substr($_SERVER["HTTP_USER_AGENT"],0,9);
echo " - ";
echo $ora;
echo " - ";
echo "User: ".$_SESSION['user'] ;

echo "</BODY>";
echo "</HTML>";
?>

