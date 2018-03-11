<?php
$username="root";
$password="root";
$database="mapData";
// Gets data from URL parameters.
$name = $_GET['name'];
$description = $_GET['description'];
$lat = $_GET['lat'];
$lng = $_GET['lng'];

// Opens a connection to a MySQL server.
$connection = new mysqli('localhost', $username, $password,$database);
// $connection=mysql_connect("localhost:3306", $username, $password);
// Inserts new row with place data.


$query = sprintf("INSERT INTO markers (`id`, `name`, `description`, `lat`, `lng` ) VALUES (NULL, '%s', '%s', '%s', '%s');",
         $name,
         $description,
         $lat,
         $lng);

$result = $connection->query($query);

if (!$result) {
  die('Invalid query: ' . mysqli_error());
  
}

?>