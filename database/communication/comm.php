<?php
/**
 * Created by PhpStorm.
 * User: yigido
 * Date: 6/23/18
 * Time: 5:19 PM
 */


$id = $_POST["id"];
$value = $_POST["value"];
$file_loc =  "../content/" .  $value . "/" . $id . ".json";
$myfile = fopen($file_loc, "r") or die("Unable to open file!");
$content = fread($myfile,filesize($file_loc));
echo $content;

?>





