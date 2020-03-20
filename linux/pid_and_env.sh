#!/usr/bin/bash

echo PID
echo $$
echo $$BASHPID

./set_env_and_process /home/gliang/prima/linux/pid_simple.sh &>/dev/null &
PID=$$BASHPID
LOG=/tmp/${PID}.log
printenv>$LOG
echo $LOG
