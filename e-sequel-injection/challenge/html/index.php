<?php

if (isset($_GET['source'])) {
    highlight_file(__FILE__);
    exit;
}

$pattern = '/(\s|UNION|OR|=|TRUE|FALSE|>|<|IS|LIKE|BETWEEN|REGEXP|--|#|;|\/|\*|\|)/i';
if (isset($_POST['username']) && isset($_POST['password'])) {

    if (preg_match($pattern, $_POST['username'], $matches)) {
        var_dump($matches);
        exit;
    }
    if (preg_match($pattern, $_POST['password'], $matches)) {
        var_dump($matches);
        exit;
    }

    $pdo = new PDO('mysql:host=e_sequel_db;dbname=e_sequel;charset=utf8;', 'e_sequel', 'e_sequelpassword');
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    $stmt = $pdo->prepare("SELECT username from users where username='${_POST['username']}' and password='${_POST['password']}'");
    $stmt->execute();
    $result = $stmt->fetchAll();
    if (count($result) > 0) {
        if ($result[0]['username'] == 'admin') {
            echo include('flag.php');
        } else {
            echo 'Nice login, ' .  $result[0]['username'] . '!';
        }
        exit;
    }
    echo 'Failed to Login';
    exit;
}

?>
<!doctype html>
<html>
	<head>
		<title>E-Sequel-Injection!</title>
		<meta charset="utf-8">
        <style>
html,body {
    width: 100%;
    height: 100%;
    display: flex;
    margin: 0;
    padding: 0;
    background-color: palevioletred;
}
#wrapper {
    width: 640px;
    margin: auto;
    border: 2px solid #000;
    padding: 20px;
    background-color: #fff;
}
input[type=text],input[type=password] {
    font-size: 120%;
    display: block;
    margin-bottom: 10px;
    padding: 0.2em;
    width: 100%;
    text-align: center;
    border: 2px solid #666;
}
input[type=submit] {
    background-color: transparent;
    box-shadow: 0 2px 1px #666;
    border: 2px solid #666;
    font-size: 120%;
    float: right;
}
input[type=submit]:hover {
    cursor: pointer;
}
input[type=submit]:active {
    position: relative;
    box-shadow: none;
    top: 2px;
}
        </style>
	</head>
	<body>
        <div id="wrapper">
            <p>just login as 'admin' by E-Sequel-Injection. <a href="?source">view source</a></p>

            <form method="POST">
                <input type="text" name="username" required placeholder="username">
                <input type="password" name="password" required placeholder="password">
                <input type="submit" value="Login">
            </form>
        </div>
	</body>
</html>
