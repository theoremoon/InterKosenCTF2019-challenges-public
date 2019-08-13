#!/bin/bash

P="0x1234"
first=$(python3 enc.py "Bl00m_1n70_Y0u" $P)
second=$(python3 enc.py "THE IDOLMA@STER" $P)
third=$(python3 enc.py "Saya YAKUSHIJI" $P)

sed -i -E "$(printf 's/(.+)first = "(.+)";/\\1first = "%s";/' "$first")" main.c
sed -i -E "$(printf 's/(.+)second = "(.+)";/\\1second = "%s";/' "$second")" main.c
sed -i -E "$(printf 's/(.+)third = "(.+)";/\\1third = "%s";/' "$third")" main.c
mkdir -p distfiles
gcc main.c -o distfiles/favorites
