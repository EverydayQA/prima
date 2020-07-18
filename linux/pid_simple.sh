#!/usr/bin/bash

echo start pid_simple.sh
echo PID $$

echo script name: $0
SPID=$$BASHPID
SLOG=/tmp/${SPID}.log
printenv>$SLOG
echo $SLOG

# run script once, no need to change
perl /home/gliang/prima/perl_path/test_path.pl
python /home/gliang/prima/app_psutil.py
# run script every 15 minutes 
echo "Bash version ${BASH_VERSION}..."
for i in {1..3}
do
    echo "Welcome $i times, execute sth, sleep 60 seconds"
    sleep 60s
done
echo end of pid_simple.sh
