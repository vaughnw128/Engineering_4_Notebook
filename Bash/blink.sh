#!/bin/bash

gpio mode 0 out

for i in $(seq 1 10)
do
	gpio write 0 1
	sleep 1
	gpio write 0 0
	sleep 1
done
