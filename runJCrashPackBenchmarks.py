#!/bin/python
import sys
import subprocess
from jcrashpack import *
import signal
import time

globals = {"process" : None}
def get_process():
    return globals["process"]

def set_process(value):
    globals["process"] = value

def sigint_handler(signum, frame):
    current = get_process()
    res = input("\nDo you want to kill the whole process or just current run? [whole/current]\n")
    if res == "whole":
        exit(1)
    elif res == "current":
        if current is None:
            print("Error, there is no process that is currently running")
        else:
            current.terminate()
            print("Successfully killed current process")
    else:
        print("Error, invalid input")

signal.signal(signal.SIGINT, sigint_handler)

jcrashpack_path = sys.argv[1]

default_depth = 0
if len(sys.argv) > 2:
    default_depth = int(sys.argv[2])

def run_benchmark(class_path: str, trace_file: str, output_directory: str, depth: int) -> bool:
    current = subprocess.Popen(
        [
            "./kex.py",
            "--classpath", "\"{}\"".format(class_path),
            "--trace", "\"{}\"".format(trace_file),
            "--mode", "crash",
            "--output", output_directory,
            "--depth", str(depth)
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    set_process(current)
    stdout, stderr = current.communicate()
    stderr_str = stderr.decode()
    return_code = current.returncode
    if return_code == 0:
        return True
    else:
        print(stderr_str)
        return False


crashes = read_crashes(jcrashpack_path)
print(len(crashes))
start = False
for name in crashes:
    # if name == 'LANG-20b':
    #     start = True
    # if not start:
    #     continue
    print("Running on benchmark {}".format(name))
    description = crashes[name]
    class_path = get_class_path(jcrashpack_path, description["application"], description["version"])
    trace_file = get_trace(jcrashpack_path, description["application"], description["id"])
    run_benchmark(class_path, trace_file, os.path.join("temp", name), default_depth)
    sys.stdout.flush()
