#!/bin/bash

directory_list=$(ls | grep -Ev  '.* | *.sh | *.py' | egrep -v "Secrets")

cd ~/Git/
for i in $directory_list; do cd $i && pwd && git pull && printf " ==== BREAK FOR NEW PULL ====\n" && cd .. ; done
