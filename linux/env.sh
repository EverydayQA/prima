#!/usr/bin/env bash

PATH='/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/home/joe/.local/bin:/home/joe/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/home/joe/.local/bin:/home/joe/bin'

function join { local IFS="$1"; shift; echo "$*"; }

function remove_if_match() {
    # uniq list of array without changing order
    env_str=$1
    match=$2

    declare -A items=()

    IFS=$':'; set $1; 
    for item; do 
	if [[ $item = *$match* ]]; then
	    continue
	fi
        items[$item]=1
    done; 
    IFS=$oIFS;

    L=${!items[*]}
    echo ${L// /:}
}

function unique_str() {
    # uniq list of array without changing order
    env_str=$1
    declare -A items=()

    IFS=$':'; set $1; 
    for item; do 
        items[$item]=1
    done; 
    IFS=$oIFS;

    L=${!items[*]}
    echo ${L// /:}
}

function append_front() {
    echo $1:$2
}

function append_last() {
    echo $2:$1
}

function array2envstr() {
    # array to envstr
    L=$1
    echo ${L// /:}
}

function elementExists() {
    elements=${1}
    element=${2}
    for i in ${elements[@]} ; do
        if [ $i == $element ] ; then
            return 1
        fi
    done
    return 0
}

function is_item_in() {
    declare -A array
    for constant in foo bar baz
    do
         array[$constant]=1
    done

    # test for existence
    test1="bar"
    test2="xyzzy"

    if [[ ${array[$test1]} ]]; then echo "Exists"; fi    # Exists
    if [[ ${array[$test2]} ]]; then echo "Exists"; fi    # doesn't
}

function echo_var() {
    echo $1 $2
}

function export_var() {
    export $1=$2
}

path='PATH'
echo $PATH
PATH_NEW=$(unique_str $PATH)
echo_var $path $PATH_NEW

echo '1 str_to_be_append'
FIRST=/home/joe/ven27p2u/bin
PATH_NEW=$(append_front $FIRST $PATH_NEW)
echo_var $path $PATH_NEW

echo 'append_last'
PATH_NEW=$(append_last $FIRST $PATH_NEW)
echo_var $path $PATH_NEW

echo 'remove items if match joe e.g python2.6'
PATH_NEW=$(remove_if_match $PATH_NEW 'joe')
echo_var $path $PATH_NEW

echo 'export_var_value'
export_var $path $PATH_NEW

echo 'parameters opts parsing case switch to be added'
