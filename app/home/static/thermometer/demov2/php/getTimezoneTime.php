<?php
    
    $tzTxt = $_REQUEST['thisTz'];
    
    $date = new DateTime();
    $tz = new DateTimeZone($tzTxt);
    $date->setTimezone($tz);
    echo $date->format(Z);
    //echo $date;
    
?>