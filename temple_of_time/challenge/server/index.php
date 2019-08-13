<?php
session_start();

if (empty($_SESSION['user'])) {
    header("Location: /login.php");
    exit(0);
}

try {
    $dsn = "mysql:host=localhost;dbname=temple;";
    $db = new PDO($dsn, 'monk', 'password');
} catch(PDOException $e) {
    echo $e->getMessage();
    exit;
}

if (!empty($_GET['portal'])) {
    $sth = $db->prepare("UPDATE Vote SET count=count+1 WHERE name='".$_GET['portal']."'");
    $sth->execute();
    $message = "Vote done!";
}
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Temple of Time</title>
    </head>
    <body style="text-align: center;">
        <h1>Temple of Time</h1>
        <hr>
        <p>Which one do you prefer?</p>
        <ul>
            <li><a href="/?portal=remembrance">Remembrance</a></li>
            <li><a href="/?portal=repentance">Repentance</a></li>
            <li><a href="/?portal=forgetfulness">Forgetfulness</a></li>
        </ul>
        <?php if (isset($message)) { ?><p><?php echo $message; ?></p><?php } ?>
    </body>
</html>
