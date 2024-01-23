#!/bin/python3

import sys
import subprocess
import json
import os
import shutil

from juge_common import *

juge_path = sys.argv[1]

mode = "concolic"

if len(sys.argv) > 2:
    mode = sys.argv[2]

coverage_file = "coverage.json"
if len(sys.argv) > 3:
    coverage_file = sys.argv[3]

benchmark_version = 10
if len(sys.argv) > 4:
    benchmark_version = int(sys.argv[4])

benchmarks = []
if benchmark_version == 10:
    benchmarks = BENCHMARK_CLASSES_10
elif benchmark_version == 11:
    benchmarks = BENCHMARK_CLASSES_11
elif benchmark_version == 12:
    benchmarks = BENCHMARK_CLASSES_12
else:
    sys.exit("Benchmark version not supported")


def execute_benchmark(project_name: str, klass_name: str, mode_name: str, output_directory: str):
    classpath = get_classpath_by_project(juge_path, project_name)
    return subprocess.run(
        [
            "python3",
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

if os.path.exists(coverage_file):
    os.remove(coverage_file)

for (index, benchmark) in enumerate(benchmarks):
    (project, klass) = benchmark
    output_dir = os.path.join("temp/", project.lower() + str(index))
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    print("Executing benchmark {} of {}: class {} of project {}"
          .format(index + 1, len(benchmarks), klass, project))
    execute_benchmark(project, klass, mode, output_dir)

coverageData = json.loads(open(coverage_file).read())

lines = 0.0
branches = 0.0
instructions = 0.0

for (project, klass) in benchmarks:
    for index in range(0, len(coverageData), 2):
        if coverageData[index]['first'] == "class {}".format(klass.replace('.', '/')) \
                and coverageData[index]['second'] == mode:
            lines += coverageData[index + 1]['lines']
            branches += coverageData[index + 1]['branches']
            instructions += coverageData[index + 1]['instructions']
            break

print("Average line coverage: {:.2f}".format(lines / len(benchmarks)))
print("Average branch coverage: {:.2f}".format(branches / len(benchmarks)))
print("Average instruction coverage: {:.2f}".format(instructions / len(benchmarks)))
