#!/bin/python
import sys
import json
import os.path
import subprocess

jcrashpack_path = sys.argv[1]

default_depth = 3
if len(sys.argv) > 2:
    default_depth = int(sys.argv[2])


def read_crashes() -> dict:
    json_path = os.path.join(jcrashpack_path, "jcrashpack.json")
    crash_pack = json.loads(open(json_path).read())
    return crash_pack['crashes']


def get_class_path(project: str, version: str) -> str:
    project_path = os.path.join(jcrashpack_path, "applications", project, version, "bin")
    jar_files = []
    for file in os.listdir(project_path):
        file_path = os.path.join(project_path, file)
        if os.path.isfile(file_path) and file_path.endswith(".jar"):
            jar_files.append(file_path)
    return ":".join(jar_files)


def get_trace(project: str, crash_id: str) -> str:
    return os.path.join(jcrashpack_path, "crashes", project, crash_id + ".log")


def run_benchmark(class_path: str, trace_file: str, output_directory: str, depth: int) -> bool:
    process = subprocess.Popen(
        [
            "./kex.sh",
            "--classpath", class_path,
            "--trace", trace_file,
            "--mode", "crash",
            "--output", output_directory,
            "--depth", depth
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


crashes = read_crashes()
for name in crashes:
    print("Running on benchmark {}".format(name))
    description = crashes[name]
    class_path = get_class_path(description["application"], description["version"])
    trace_file = get_trace(description["application"], description["id"])
    if not run_benchmark(class_path, trace_file, os.path.join("temp", name), default_depth):
        break

