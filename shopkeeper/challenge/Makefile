all:
	gcc -Wl,-z,relro,-z,now main.c -o chall -pie -fno-stack-protector
	cp ./chall ../distfiles/chall
	cp ./main.c ../distfiles/shopkeeper.c
