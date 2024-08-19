import subprocess
import re

#format 2024/08/18 21:58:35.907, 4.69
def get_power(output):
    numbers = re.findall(r'\d+',output)
    #print(numbers)
    p = numbers[-2:]
    #print(p)
    power = float(p[0]) + float(p[1]) / 1000.0
    #print(power)
    return power

#command = ["sudo","./tegrastats", "--interval", "1000" "--verbose"]
interval = 1
command = ["nvidia-smi", "--query-gpu=timestamp,power.draw", 
           "--format=csv,noheader,nounits", "-l", "1.2"]
process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
while True:
    output = process.stdout.readline()
    print(output)
    #result0 = str(output)
    print(get_power(str(output)))


