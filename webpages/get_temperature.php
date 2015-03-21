<?php

exec("cat /home/pi/CicloAcqua/temperature.out",$output);
#echo $output;
foreach ($output as $result) {
   echo $result;
}

?>

