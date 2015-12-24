#!/usr/bin/python
import json
import subprocess
from subprocess import check_output
result = json.loads(check_output(["php","./mini.php"]).decode('utf-8'))

