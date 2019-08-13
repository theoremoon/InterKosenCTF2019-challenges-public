<?php

ini_set('display_errors', 0);

// reset challenge environment hourly
if (!file_exists('../hourly') || (time() - filemtime('../hourly')) > 60*60) {
    // remove uploaded files
    foreach (glob('../files/*') as $f) {
        unlink("../files/$f");
    }
    rmdir('../files');

    // remove a database
    unlink('../database.db');

    // make a directory to store uploaded files
    mkdir('../files');

    // move a secret file into `files`
    copy('../secret_file', '../files/secret_file');

    // make the database
    $db = new PDO('sqlite:../database.db');
    $db->exec('CREATE TABLE files(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, passcode TEXT)');

    // create a secret entry
    $secrets = include('secrets.php');
    $db->exec("INSERT INTO files(name, passcode) VALUES ('secret_file', '{$secrets['passcode']}')");

    // update file modified time
    file_put_contents('../hourly', (string)time());
}

if (isset($_GET['source'])) {
    highlight_file(__FILE__);
    exit;
}

$db = new PDO('sqlite:../database.db');

// when a file is uploaded
if (isset($_POST['passcode'])) {
    $filename = basename($_FILES['file']['name']);
    if (!preg_match('@^[A-Za-z0-9_.]+$@', $filename)) {
        die('Invalid Filename');
    }
    $uploadfile = '../files/' . $filename;
    if (file_exists($uploadfile)) {
        die('File already exists');
    }
    if (! move_uploaded_file($_FILES['file']['tmp_name'], $uploadfile)) {
        die('Failed to upload file');
    }
    $db->exec("INSERT INTO files(name, passcode) VALUES ('$filename', '{$_POST['passcode']}')");
}

// file download query
if (isset($_GET['download']) && isset($_GET['passcode'])) {
    $name = $_GET['download'];
    $rows = $db->query("select name, passcode from files where name = '$name'")->fetchAll();
    if (count($rows) == 1 && $rows[0][0] === $name && $rows[0][1] == $_GET['passcode']) {
        $path = '../files/'. $name;
        header('Content-Type: application/force-download');
        header('Content-Length: '.filesize($path));
        header('Content-disposition: attachment; filename="'.$name.'"');
        readfile($path);
        exit;
    } else {
        die('Invalid filename or passcode');
    }
}

$files = [];
// search
if (isset($_GET['search'])) {
    $rows = $db->query("SELECT name FROM files WHERE instr(name, '{$_GET['search']}') ORDER BY id DESC");
    foreach ($rows as $row) {
        $files []= $row[0];
    }
}
// all files
else {
    $rows = $db->query('SELECT name FROM files ORDER BY id DESC');
    foreach ($rows as $row) {
        $files []= $row[0];
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>UPLOADER</title>
    <style>
.container {
    width: 1024px;
    margin: 0 auto;
}
h1 {
    text-align: center;
}
section {
    margin: 20px 0;
}
h2 {
    border-bottom: 1px solid #ccc;
}
input[type=file] {
    display: none;
}
.upload,input[type=submit] {
    border: 1px solid #ccc;
    display: inline-block;
    padding: 0.5em 2em;
    cursor: pointer;
}
input[type=text],input[type=password] {
    border: 1px solid #ccc;
    padding: 0.5em;
}
li {
    clear: both;
}
.inline-form {
    display: inline-block;
    float: right;
}
    </style>
</head>
<body>
    <div class="container">
    <h1>UPLOADER</h1>
    <p><a href="?source">view source</a></p>

<section>
        <h2>UPLOAD</h2>
        <form enctype="multipart/form-data" method="POST">
            <label for="file-upload" class="upload">file upload</label>
            <input name="file" type="file" id="file-upload"/>
            passcode: <input type="password" name="passcode" required>
            <input type="submit" value="UPLOAD" />
        </form>
</section>

<section>
        <h2>DOWNLOAD</h2>
        <form method="GET"><input type="text" name="search" value="<?= @$_GET['search']; ?>"><input type="submit" value="search by keyword"></form>

        <ul>
            <?php foreach ($files as $f) {
            echo "<li>$f<form class='inline-form' method='get'><input type='hidden' name='download' value='$f'>passcode: <input type='password' name='passcode'/><input type='submit' value='download'></form></li>";
            } ?>
        </ul>
</section>
    </div>
</body>
</html>
