<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News page</title>
    <style type="text/css">
        *{
            margin: 0;
            padding: 0;
        }
        .box{
            overflow :  hidden;
            width: 100%;
            height: 100vh;
            background-image: url();
            background-size: cover;
            text-align: center;
        }
        .top{
            height : 7px;
            background-color : black;
        }
        image{
            float : left;
        }
        div{

        }
    </style>
</head>
<body>
<h1> Agro News Feed </h1>
<br><br><hr class = "top">
<?php
        $file = fopen("news.txt", "r") or die ("Im drowning ... Let me die");
        $content = fread($file ,filesize("news.txt"));
        fclose($file);
        $textArray = explode("\n",$content) ;
        $count =0;
        foreach ($textArray as $key=>$value) {
        echo "<br>";
        $key ++;
        if($count == 0){
            echo "<div>";
            echo "<h2>$value<br></h2>";
            $count+=1;
        }
        else if ($count == 1){
            echo "<a href=$value>Link<br></a>";
            $count+=1;
        }
        else if ($count == 2){
            echo "<img src = $value><br>";
            $count = 0;
        echo "</div>";
        echo "<br><hr>";
        }

        }
?>
</body>
</html>
