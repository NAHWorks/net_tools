import argparse
import socket
import shlex 
import subprocess 
import sys
import textwrap 
import threading 

# This is a function which will execute commands and return the output. 
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()

# Main block for handling command line arguments and calling the rest of the functions.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class==argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
            netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.whatisup # upload to file
            netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" #execute command 
            echo 'ABCDEFGHI' | ./netcat.py -t 192.168.1.108 -p 135 # echo local text to server port 135
            netcat.py -t 192.168.1.108 -p 5555 # connect to server
        '''))
      