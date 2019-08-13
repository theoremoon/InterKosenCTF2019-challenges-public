<?php
if (empty($_POST['ext']) || empty($_POST['name'])) {
    // Missing parameter(s)
    header("HTTP/1.1 404 Not Found");
    print("404 Not Found");
    exit;
} else {
    $ext = strtolower($_POST['ext']);   // Extension
    $name = strtolower($_POST['name']); // Filename
}

if (strlen($ext) > 4) {
    // Invalid extension
    header("HTTP/1.1 500 Internal Server Error");
    print("500 Internal Server Error");
    exit;
}

switch($ext) {
    case 'jpg':
    case 'jpeg': $mime = 'image/jpg'; break;
    case 'png': $mime = 'image/png'; break;
    default: $mime = 'application/force-download';
}

// Download
header('Expires: 0');
header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
header('Cache-Control: private', false);
header('Content-Type: '.$mime);
header('Content-Transfer-Encoding: binary');
include($ext.'/'.$name.'.'.$ext);
?>
