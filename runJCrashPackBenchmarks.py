#!/bin/python
import sys
import subprocess
from jcrashpack import *

excludes = {'ES-18109', 'ES-19414', 'ES-21665', 'ES-21911', 'ES-22077', 'ES-22997', 'ES-23115', 'ES-24047', 'ES-24485',
            'ES-24968', 'ES-25119', 'ES-25359', 'ES-25666', 'ES-25775', 'ES-25905', 'ES-26191', 'ES-26865', 'ES-26868',
            'ES-27788', 'ES-28141',  'ES-9379', 'LANG-13b', 'LANG-44b', 'MATH-101b', 'MATH-31b', 'MATH-60b', 'MATH-85b', 'LANG-27b',
            'MOCKITO-17b', 'MOCKITO-21b', 'MOCKITO-23b', 'MOCKITO-4b', 'TIME-14b', 'TIME-18b', 'XRENDERING-481', 'XWIKI-13137',
            'XWIKI-13407', 'XWIKI-13617', 'XWIKI-13916', 'XWIKI-13942', 'XWIKI-14263', 'XWIKI-14599', 'XWIKI-14612', 'XWIKI-13031'
            'ES-23675', 'XWIKI-13031'}

jcrashpack_path = sys.argv[1]

default_depth = 3
if len(sys.argv) > 2:
    default_depth = int(sys.argv[2])

def run_benchmark(class_path: str, trace_file: str, output_directory: str, depth: int) -> bool:
    process = subprocess.Popen(
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
    stdout, stderr = process.communicate()
    stderr_str = stderr.decode()
    if process.returncode == 0:
        return True
    else:
        print(stderr_str)
        return False


crashes = read_crashes(jcrashpack_path)
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
