#!/bin/bash

servers=1,2,3,4,5,6,7,8,9,10
OIFS=${IFS}
IFS=","
counter=1
for server in ${servers}
do
    [ "${counter}" -ge 1 -a "${counter}" -le 4 ]  && echo function1 ${server}
    [ "${counter}" -ge 5 -a "${counter}" -le 8 ]  && echo function2 ${server}
    [ "${counter}" -ge 9 -a "${counter}" -le 10 ] && echo function3 ${server}
    ((counter++))
     echo $counter
done
#IFS=$OIFS;

#IFS=, read -a server_list <<< "$servers"

batch_size=4
for ((i=0; i<=${#servers[@]}; i+=batch_size)); do
    echo function1 "${server_list[@]:i:i+batch_size}"
    echo function2 "${server_list[@]:i:i+batch_size}"
    echo function3 "${server_list[@]:i:i+batch_size}"
done

servers=1,2,3,4,5,6,7,8,9,10

counter=1
for server in ${servers}

    do
        counter=$((counter+1))

        echo $server
        if [ "$counter" -gt 4 ]; then
            break
        fi
    done

