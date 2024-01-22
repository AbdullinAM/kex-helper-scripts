#!/bin/python3

import sys
import json

from juge_common import *

coverage_file = "coverage.json"
if len(sys.argv) > 1:
    coverage_file = sys.argv[1]

mode = "concolic"
if len(sys.argv) > 2:
    mode = sys.argv[2]

BENCHMARK_CLASSES = BENCHMARK_CLASSES_10
if len(sys.argv) > 3:
    version = int(sys.argv[3])
    if version == 10:
        BENCHMARK_CLASSES = BENCHMARK_CLASSES_10
    elif version == 11:
        BENCHMARK_CLASSES = BENCHMARK_CLASSES_11
    elif version == 12:
        BENCHMARK_CLASSES = BENCHMARK_CLASSES_12
    else:
        sys.exit("Benchmark version not supported")

coverageData = json.loads(open(coverage_file).read())

lines = 0.0
branches = 0.0
instructions = 0.0

uncovered_classes = []



for (project, klass) in BENCHMARK_CLASSES:
    found = False
    for index in range(0, len(coverageData), 2):
        if coverageData[index]['first'] == "class {}".format(klass.replace('.', '/')) \
                and coverageData[index]['second'] == mode:
            lines += coverageData[index + 1]['lines']
            branches += coverageData[index + 1]['branches']
            instructions += coverageData[index + 1]['instructions']

            print(
                "{}: {} - {:.2f} lines, {:.2f} branches, {:.2f} instructions"
                .format(
                    project, klass,
                    coverageData[index + 1]['lines'],
                    coverageData[index + 1]['branches'],
                    coverageData[index + 1]['instructions']
                )
            )
            found = True
            break

    if not found:
        print("{}: {} - coverage information not found".format(project, klass))
        uncovered_classes.append(klass)

print()
print("Average line coverage for all classes: {:.2f}".format(lines / len(BENCHMARK_CLASSES)))
print("Average branch coverage for all classes: {:.2f}".format(branches / len(BENCHMARK_CLASSES)))
print("Average instruction coverage for all classes: {:.2f}".format(instructions / len(BENCHMARK_CLASSES)))
if len(uncovered_classes) != 0:
    number_found = len(BENCHMARK_CLASSES) - len(uncovered_classes)
    print()
    print("Average line coverage for found classes: {:.2f}".format(lines / number_found))
    print("Average branch coverage for found classes: {:.2f}".format(branches / number_found))
    print("Average instruction coverage for found classes: {:.2f}".format(instructions / number_found))
    print()
    print("Uncovered classes:")
    print("\n".join(uncovered_classes))
