tshark -r ../distfiles/*.pcapng -Tfields -e http.response_for.uri  -Y 'http.response and http.time > 1' > queries.txt
python3 solve.py
rm queries.txt
