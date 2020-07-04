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
# conda or virtualenv -- is this the right way?
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
# “a” and “arga” have optional arguments with default values.
# “b” and “argb” have no arguments, acting as sort of a flag.
# “c” and “argc” have required arguments.

# set an initial value for the flag
ARGB=0

# read the options
TEMP=`getopt -o a::bc: --long arga::,argb,argc: -n 'test.sh' -- "$@"`
eval set -- "$TEMP"

# extract options and their arguments into variables.
while true ; do
    case "$1" in
        -a|--arga)
            case "$2" in
                "") ARGA='py37' ; shift 2 ;;
                *) ARGA=$2 ; shift 2 ;;
            esac ;;
        -b|--argb) ARGB=1 ; shift ;;
        -c|--argc)
            case "$2" in
                "") shift 2 ;;
                *) ARGC=$2 ; shift 2 ;;
            esac ;;
        --) shift ; break ;;
        *) echo "Internal error!" ; exit 1 ;;
    esac
done

# do something with the variables -- in this case the lamest possible one :-)
echo "ARGA = $ARGA"
echo "ARGB = $ARGB"
echo "ARGC = $ARGC"
if [ $ARGA -eq "py37"]
    source /home/gliang/.py37_env.sh
then
    echo "not default py37"
fi
