all:
	gcc main.c -o saferm
	touch disk.img

initialize:
	mkdir /tmp/disk
	make mkdisk
	make mkpart
	make mkfs
	make mnt
	make create
	make clean
	rm /tmp/disk -r

mkdisk:
	dd if=/dev/zero of=disk.img bs=1M count=10

mkpart:
	sudo losetup /dev/loop100 disk.img
	sudo parted -s -a optimal /dev/loop100 mklabel msdos
	sudo parted -s -a optimal /dev/loop100 mkpart primary 0% 100%
	sudo parted /dev/loop100 p

mkfs:
	sudo mkfs -t ntfs /dev/loop100p1
	sudo parted /dev/loop100 p

mnt:	
	sudo mount -t ntfs /dev/loop100p1 /tmp/disk
	df -Th

create:
	sudo cp document.zip /tmp/disk/document.zip
	sudo cp saferm /tmp/disk/saferm
	sudo sync
	sudo /tmp/disk/saferm /tmp/disk/document.zip
	sudo dd if=/dev/loop100 of=dump.bin bs=1M count=10
	sudo sync

clean:
	sudo umount disk
	sudo losetup -d /dev/loop100
