#!/usr/bin/python
import subprocess
cmd = './mini.php'
process = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
response = process.stdout.read()
print response
