#!/bin/bash
VALUE=$1

if [[ -z $VALUE ]];then
    echo "[!] You need pass some value !!"
    exit
else
    for i in $(find . -name $VALUE); do
        echo $i;
    done
    echo "[+] All $VALUE removed !!"
fi