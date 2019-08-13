gcc solve.c -o solve && ./solve | ./favorites | grep -o -E "KosenCTF{.+}"
rm solve
