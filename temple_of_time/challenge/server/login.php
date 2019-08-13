<?php
session_start();

try {
    $dsn = "mysql:host=localhost;dbname=temple;";
    $db = new PDO($dsn, 'monk', 'password');
} catch(PDOException $e) {
    echo $e->getMessage();
    exit;
}

if (!empty($_POST['user']) && !empty($_POST['pass'])) {
    $sth = $db->prepare("SELECT * FROM Users WHERE username='".$_POST['user']."' AND password='".$_POST['pass']."'");
    $sth->execute();
    $result = $sth->fetch(PDO::FETCH_ASSOC);
    print_r($result);
    if ($result) {
        $_SESSION['user'] = $result['username'];
        header("Location: /index.php");
        exit(0);
    }
}
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Login - Temple of Time</title>
    </head>
    <body>
        <h1 style="text-align: center;">Login</h1>
        <hr>
        <p>You need to login before voting.</p>
        <form action="/login.php" method="POST">
            <label>Username: </label>
            <input type="text" name="user"><br>
            <label>Password: </label>
            <input type="password" name="pass"><br>
            <input type="submit" value="Login">
        </form>
    </body>
</html>
