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

mode = "concolic"

if len(sys.argv) > 2:
    mode = sys.argv[2]

coverage_file = "coverage.json"
if len(sys.argv) > 3:
    coverage_file = sys.argv[3]

delete_coverage = False
if len(sys.argv) > 4:
    delete_coverage = bool(sys.argv[4])

start = True
start_from = ""
if len(sys.argv) > 5:
    start = False
    start_from = sys.argv[5]


def execute_benchmark(project_name: str, klass_name: str, mode_name: str, output_directory: str):
    classpath = ""
    if project_name == "FASTJSON":
        classpath = fastjson_classpath(juge_path)
    elif project_name == "GUAVA":
        classpath = guava_classpath(juge_path)
    elif project_name == "SEATA":
        classpath = seata_classpath(juge_path)
    elif project_name == "SPOON":
        classpath = spoon_classpath(juge_path)
    return subprocess.run(
        [
            "python",
            "./kex.py",
            "--classpath", classpath,
            "--target", klass_name,
            "--mode", mode_name,
            "--output", output_directory,
            "--option", "kex:coverage:{}".format(coverage_file)
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


if delete_coverage and os.path.exists(coverage_file):
    os.remove(coverage_file)


for (index, benchmark) in enumerate(BENCHMARK_CLASSES):
    (project, klass) = benchmark
    if klass == start_from:
        start = True

    if not start:
        continue

    output_dir = os.path.join("temp/", project.lower())
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    print("Executing benchmark {} of {}: class {} of project {}"
          .format(index + 1, len(BENCHMARK_CLASSES), klass, project))
    execute_benchmark(project, klass, mode, output_dir)

coverageData = json.loads(open(coverage_file).read())

lines = 0.0
branches = 0.0
instructions = 0.0

for (project, klass) in BENCHMARK_CLASSES:
    for index in range(0, len(coverageData), 2):
        if coverageData[index]['first'] == "class {}".format(klass.replace('.', '/')) \
                and coverageData[index]['second'] == mode:
            lines += coverageData[index + 1]['lines']
            branches += coverageData[index + 1]['branches']
            instructions += coverageData[index + 1]['instructions']
            break

print("Average line coverage: {:.2f}".format(lines / len(BENCHMARK_CLASSES)))
print("Average branch coverage: {:.2f}".format(branches / len(BENCHMARK_CLASSES)))
print("Average instruction coverage: {:.2f}".format(instructions / len(BENCHMARK_CLASSES)))
