<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Neko Loader</title>
    </head>
    <body style="text-align: center;">
        <h1>Neko Loader</h1>
        <hr>
        <p>- Nyan Presents -</p>
        <form action="/getimage.php" method="POST">
            <label>Extension: </label>
            <select name="ext">
                <option value="png">PNG</option>
                <option value="jpeg">JPEG</option>
            </select>
            <br>
            <label>File: </label>
            <select name="name">
                <option value="inter_neko">Inter Neko</option>
                <option value="winter_neko">Winter Neko</option>
                <option value="dot_neko">Dot Neko</option>
            </select>
            <br><br>
            <input type="submit" value="Download">
        </form>
    </body>
</html>
