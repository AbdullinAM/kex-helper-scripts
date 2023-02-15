#!/bin/python
import sys
import subprocess
from jcrashpack import *

jcrashpack_path = sys.argv[1]

default_depth = 3
if len(sys.argv) > 2:
    default_depth = int(sys.argv[2])

def run_benchmark(class_path: str, trace_file: str, output_directory: str, depth: int) -> bool:
    process = subprocess.Popen(
        [
            "./kex.sh",
            "--classpath", class_path,
            "--trace", trace_file,
            "--mode", "crash",
            "--output", output_directory,
            "--depth", str(depth)
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    stderr_str = stderr.decode()
    if process.returncode == 0:
        return True
    else:
        print(stderr_str)
        return False


crashes = read_crashes(jcrashpack_path)
for name in crashes:
    print("Running on benchmark {}".format(name))
    description = crashes[name]
    class_path = get_class_path(jcrashpack_path, description["application"], description["version"])
    trace_file = get_trace(jcrashpack_path, description["application"], description["id"])
    if not run_benchmark(class_path, trace_file, os.path.join("temp", name), default_depth):
        break

