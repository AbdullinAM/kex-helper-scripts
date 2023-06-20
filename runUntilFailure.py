#!/bin/python

import sys
import subprocess
import json
import os
import shutil

from juge10 import BENCHMARK_CLASSES
from juge10 import fastjson_classpath
from juge10 import guava_classpath
from juge10 import seata_classpath
from juge10 import spoon_classpath

juge_path = sys.argv[1]

startIndex = 0
mode = "concolic"

if len(sys.argv) > 2:
    mode = sys.argv[2]

coverage_file = "coverage.json"
if len(sys.argv) > 3:
    coverage_file = sys.argv[3]

delete_coverage = False
if len(sys.argv) > 4:
    delete_coverage = bool(sys.argv[4])


def test_benchmark(project_name: str, klass_name: str, mode_name: str, output_directory: str) -> bool:
    classpath = ""
    if project_name == "FASTJSON":
        classpath = fastjson_classpath(juge_path)
    elif project_name == "GUAVA":
        classpath = guava_classpath(juge_path)
    elif project_name == "SEATA":
        classpath = seata_classpath(juge_path)
    elif project_name == "SPOON":
        classpath = spoon_classpath(juge_path)
    process = subprocess.Popen(
        [
            "./kex.py",
            "--classpath", classpath,
            "--target", klass_name,
            "--mode", mode_name,
            "--output", output_directory,
            "--option", "kex:coverage:{}".format(coverage_file)
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    stderrStr = stderr.decode()
    if process.returncode == 0:
        return True
    else:
        print(stderrStr)
        return False


if delete_coverage and os.path.exists(coverage_file):
    os.remove(coverage_file)

for (index, benchmark) in enumerate(BENCHMARK_CLASSES):
    if index < startIndex:
        continue
    (project, klass) = benchmark
    output_dir = os.path.join("temp/", project.lower())
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    print("Executing benchmark {} of {}: class {} of project {}"
          .format(index + 1, len(BENCHMARK_CLASSES), klass, project))
    if not test_benchmark(project, klass, mode, output_dir):
        print("Failed on the benchmark class {} of project {}".format(klass, project))
        break

