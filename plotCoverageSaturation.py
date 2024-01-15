#!/bin/python3

import sys
import subprocess
import json
import os
import isodate
import matplotlib.pyplot as plt

coverage_file = "../kex/saturation-coverage.json"
if len(sys.argv) > 1:
    coverage_file = sys.argv[1]

mode = "concolic"
if len(sys.argv) > 2:
    mode = sys.argv[2]

displayed_coverages = ['lines', 'branches'] # 'instructions'

coverageData = json.loads(open(coverage_file).read())

start_time = 0
end_time = 150
time_step = 1

klass_timelines = {}

for index in range(0, len(coverageData), 2):
	klass = coverageData[index]['first']
	klass_mode = coverageData[index]['second']
	if klass_mode != mode:
		continue

	coverage_timeline = {}
	for coverages in coverageData[index + 1]:
		time = int(isodate.parse_duration(coverages['first']).total_seconds())
		# if time > end_time:
		# 	end_time = time
		coverage_timeline[time] = [coverages['second'][coverage_type] for coverage_type in displayed_coverages]

	klass_timelines[klass] = coverage_timeline

for iteration in range(start_time, end_time + time_step, time_step):
	for klass, coverage_timeline in klass_timelines.items():
		if iteration not in coverage_timeline:
			coverage_timeline[iteration] = coverage_timeline[iteration - time_step]

averaged_timelines = {}
for iteration in range(start_time, end_time + time_step, time_step):
	sums = [0.0 for _ in displayed_coverages]
	for klass, coverage_timeline in klass_timelines.items():
		for index in range(len(sums)):
			sums[index] += coverage_timeline[iteration][index]
	averaged_timelines[iteration] = [element / len(klass_timelines) for element in sums]

times = []
plots = {coverage_type: [] for coverage_type in displayed_coverages}
for iteration in range(start_time, end_time + time_step, time_step):
	times.append(iteration)
	for index, coverage_type in enumerate(displayed_coverages):
		plots[coverage_type].append(averaged_timelines[iteration][index] * 100.0)

for name, plot in plots.items():
	plt.plot(times, plot, label = "{} coverage".format(name))

# plt.plot([100 for _ in plot], plot, linestyle='dashed')

plt.xlabel('time, s')
plt.ylabel('coverage, %')
plt.title('Averaged coverage saturation')
plt.legend()
plt.grid()
plt.show()