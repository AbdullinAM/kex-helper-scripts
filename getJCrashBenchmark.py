#!/bin/python

import sys

from jcrashpack import *
from paths import JCRASHPACK_PATH

jcrashpack_path = JCRASHPACK_PATH
if len(sys.argv) > 1:
	jcrashpack_path = sys.argv[1]


benchmark = 'CHART-4b'
if len(sys.argv) > 2:
	benchmark = sys.argv[2]

depth = 0

crashes = read_crashes(jcrashpack_path)
description = crashes[benchmark]

print(description)

class_path = get_class_path(jcrashpack_path, description["application"], description["version"])
trace_file = get_trace(jcrashpack_path, description["application"], description["id"])

print("""
--classpath
"{}"
--mode
crash
--trace
"{}"
--depth
{}
--output
temp/{}
""".format(class_path, trace_file, str(depth), benchmark))
