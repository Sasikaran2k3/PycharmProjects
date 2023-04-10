<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Case</title>
    <style type="text/css">
        *{
            margin: 0;
            padding: 0;
        }
        h1{
            opacity:1;
        }
        .box{
            overflow :  hidden;
            width: 100%;
            height: 100vh;
            background-image: url(case.png);
            background-size: cover;
            text-align: center;
            opacity:0.2
        }
    </style>
</head>
<body>
    <div class="box">
        <table>
            <br><br>
            <form action="Case.php" method="post">
                <label>Details</label>
                <input type="text" name="name">
            </form>
        </table>
        <h1>Know Your Right</h1>
    </div>

</body>
</html>
