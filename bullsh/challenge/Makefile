all:
	gcc -Wl,-z,lazy main.c -o chall -fstack-protector-strong -no-pie
	cp ./chall ../distfiles/chall
	cp ./libc-2.27.so ../distfiles/libc-2.27.so
