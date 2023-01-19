#!/bin/python

import sys
import json

from juge10 import BENCHMARK_CLASSES

coverage_file = "coverage.json"
if len(sys.argv) > 1:
    coverage_file = sys.argv[1]

mode = "concolic"
if len(sys.argv) > 2:
    mode = sys.argv[2]

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
print("Average line coverage: {:.2f}".format(lines / len(BENCHMARK_CLASSES)))
print("Average branch coverage: {:.2f}".format(branches / len(BENCHMARK_CLASSES)))
print("Average instruction coverage: {:.2f}".format(instructions / len(BENCHMARK_CLASSES)))
print("Uncovered classes:")
print("\n".join(uncovered_classes))
