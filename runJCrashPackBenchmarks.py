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

excludes = {'ES-14457', 'ES-18109', 'ES-19026', 'ES-19414', 'ES-20045', 'ES-21665', 'ES-21911', 'ES-22077', 
            'ES-22156', 'ES-22373', 'ES-22500', 'ES-22997', 'ES-23115', 'ES-24047', 'ES-24485',
            'ES-24968', 'ES-25119', 'ES-25359', 'ES-25666', 'ES-25775', 'ES-25905', 'ES-26191', 'ES-26865', 'ES-26868',
            'ES-27788', 'ES-28141',  'ES-9379', 'LANG-13b', 'LANG-37b', 'MATH-8b',
            'MOCKITO-17b', 'MOCKITO-21b', 'MOCKITO-23b', 'MOCKITO-4b', 'TIME-14b', 'TIME-18b', 'XRENDERING-481', 'XWIKI-13137',
            'XWIKI-13407', 'XWIKI-13617', 'XWIKI-13916', 'XWIKI-13942', 'XWIKI-14263', 'XWIKI-14599', 'XWIKI-14612', 'XWIKI-13031'
            'ES-23675', 'XWIKI-13031'}

jcrashpack_path = sys.argv[1]

default_depth = 0
if len(sys.argv) > 2:
    default_depth = int(sys.argv[2])

def run_benchmark(class_path: str, trace_file: str, output_directory: str, depth: int) -> bool:
    current = subprocess.Popen(
        [
            "./kex.sh",
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
print(len(crashes) - len(excludes))
for name in crashes:
    if name in excludes:
        continue
    if 'ES' in name:
        continue
    if 'XWIKI' in name:
        continue
    print("Running on benchmark {}".format(name))
    description = crashes[name]
    class_path = get_class_path(jcrashpack_path, description["application"], description["version"])
    trace_file = get_trace(jcrashpack_path, description["application"], description["id"])
    run_benchmark(class_path, trace_file, os.path.join("temp", name), default_depth)
    sys.stdout.flush()
