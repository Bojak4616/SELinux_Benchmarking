#!/bin/bash

rm -f *.speeds

for i in {0..100};do
	dd if=/dev/zero of=4k.file bs=4k count=1 > /dev/null 2>&1
	pv -af 4k.file 4k.file.speed 2>&1 | cut -d"[" -f2 | cut -d"M" -f1 >> 4k.speeds
done

for i in {0..100};do
	dd if=/dev/zero of=1k.file bs=1k count=1 > /dev/null 2>&1
	pv -af 1k.file 1k.file.speed 2>&1 | cut -d"[" -f2 | cut -d"M" -f1 >> 1k.speeds
done

for i in {0..100};do
	dd if=/dev/zero of=256b.file bs=256 count=1 > /dev/null 2>&1
	pv -af 256b.file 256b.file.speed 2>&1 | cut -d"[" -f2 | cut -d"M" -f1 >> 256b.speeds
done
