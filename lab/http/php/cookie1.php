<?php

// La funzione header consente di aggiungere nuovi header.
// devono essere inserite prima di ogni tag HTML
// esempi:
// header('Location: http://www.example.com/');
// setcookie() e' un header speciale che agevola l'input dei dati:
// 

//header ("Content-Type: text/plain");
header ("Content-Type: text/html");
setcookie ("nome_cookie","val_cookie",time()+3600,"/");

$ora = date ("d M Y H:i:s");


echo "<HTML>";
echo "<BODY>";
echo "Server: ".$_SERVER["SERVER_ADDR"]; 
echo " - ";
echo "Client Address: ".$_SERVER["REMOTE_ADDR"];
echo " - ";
echo  "User Agent: ".substr($_SERVER["HTTP_USER_AGENT"],0,9);
echo " - ";
echo $ora;
echo "<p>";

if (isset($_COOKIE['nome_cookie'])) print  "Nome_Cookie: ".$_COOKIE['nome_cookie']."<p>";
if (isset($_GET['str1']))           print  "str1:        ".$_GET['str1']."<p>";
                  else              print  " str1 not set<p>";

echo "</BODY>";
echo "</HTML>";
?>

