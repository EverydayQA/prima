#!/bin/bash
box=$(hostname)
echo $box
echo $(hostname)

for file in `find . -type f -name "*.py"`; 
    do 
        dir=$(dirname $file);
        bdir=$(basename $dir);
        bname=$(basename $file);
        new=$bdir.$bname; 
        # replace 2 dots with nothing
        # bash 4.1.2 centos 6.4 no problem
        newname=${new//../}; 
        newname_with_path=$dir/$newname; 
        if [ "$file" != "$newname_with_path" ]; then
            echo mv -u $file  $newname_with_path;
        fi
    done

echo $0
echo `realpath $0`
echo `basename $0`
