#!/bin/bash
box=$(hostname)
echo $box
echo $(hostname)
FILENAME=$1
ERROR="[INPUT ERROR]"
if [ $# -lt 1 ]; then
    echo "$ERROR Need 1 input file name"
    exit 1
fi

if [ ! -f "$FILENAME" ]; then
    echo -e "$ERROR File does not exist. \n\t$FLENAME"
    exit 1
fi

