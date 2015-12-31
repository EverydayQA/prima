#!/bin/bash
box=$(hostname)
echo $box
echo $(hostname)
echo "bash version 4.1.2"
echo "centos 6.4"

for dir in `find . -type d`; 
    do 
        # match .git
        if [[ $dir != *".git"* ]]; then
            echo $dir
            gitkeep=$dir/".gitkeep"
            if [ -e "$gitkeep" ]; then
                echo "gitkeep already exist"
            else
                echo touch $gitkeep;
            fi
        else
            echo $dir
        fi
    done
