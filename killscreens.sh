#!/bin/bash
echo "Deleting all screens named $1";
for session in $(screen -ls | grep -o "[0-9]*\.${1}") 
do
	screen -S "${session}" -X quit 
done
