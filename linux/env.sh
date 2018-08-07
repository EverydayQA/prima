#!/usr/bin/env bash
echo "TEST_VAR before export is: <$TEST_VAR>"

export TEST_VAR=/opt/loca/netcdf
echo "TEST_VAR after export is: <$TEST_VAR>"
eval /sbin/ifconfig| awk '/inet addr/{print substr($2,6)}'

result=''
PATH='/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/home/gliang/.local/bin:/home/gliang/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/home/gliang/.local/bin:/home/gliang/bin'

function split_envstr() {
    # a envstr into array
    IFS=$':'; set $1; for item; do echo $item; done; IFS=$oIFS;
}

function remove_if_match() {
    # remove python2.6 or python2.7 from pythonpath
    echo 'remove_if_match'
}

function remove_items() {
    # remove items from array
    echo 'remove items'
}
function join { local IFS="$1"; shift; echo "$*"; }

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

function insert_first() {
    # add array to array
    echo 'insert_first'
}

function array2envstr() {
    # array to envstr
    echo 'array2envstr'
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
echo $PATH
# split
r=$(split_envstr $PATH)
echo $r
PATH_NEW=$(unique_str $PATH)
echo 'path-new'
echo $PATH_NEW
