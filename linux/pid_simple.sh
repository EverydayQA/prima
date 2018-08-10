#!/usr/bin/bash

echo start pid_simple.sh
echo PID $$

echo script name: $0
SPID=$$BASHPID
SLOG=/tmp/${SPID}.log
printenv>$SLOG
echo $SLOG
echo end of pid_simple.sh
