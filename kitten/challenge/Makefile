all:
	gcc -Wl,-z,now,-z,relro -fno-pie -no-pie -Xlinker --defsym -Xlinker kittens=0x6020a0 main.c -o chall -fstack-protector
	cp chall ../distfiles/chall
