#!/bin/python

import os
import json

from paths import JUGE_PATH

from juge_common import *

JUGE_HOME = os.path.join(JUGE_PATH,'infrastructure/benchmarks_12th/')
JUGE_DOCKER_HOME = '/var/benchmarks/'

def print_benchmarks(index: int, project: str, klass: str):
	print('{}-{}='.format(project, index) + '{')
	srcDir = ""
	binDir = ""
	if project == "BYTEBUDDY":
		srcDir = "/var/benchmarks/projects/byte-buddy/byte-buddy-dep/src/main/java"
		binDir = "/var/benchmarks/projects/byte-buddy/byte-buddy-dep/target/classes"
	elif project == "ERRORPRONE":
		srcDir = "/var/benchmarks/projects/error-prone/core/src/main/java"
		binDir = "/var/benchmarks/projects/error-prone/core/target/classes"
	elif project == "JAVAPOET":
		srcDir = "/var/benchmarks/projects/javapoet/src/main/java"
		binDir = "/var/benchmarks/projects/javapoet/target/classes"
	print('  src={}'.format(srcDir))
	print('  bin={}'.format(binDir))
	print('  classes=(')
	print('    {}'.format(klass))
	print('  )')
	print('  classpath=(')
	print('    {}'.format(get_classpath_by_project(JUGE_PATH, project).replace(JUGE_PATH + 'infrastructure/benchmarks_12th/', '/var/benchmarks/').replace(':', ',')))
	print('  )')
	print('}')



print('{')
index = 0
for line in BENCHMARK_CLASSES_12:
	print_benchmarks(index, line[0], line[1])
	index = index + 1
print('}')