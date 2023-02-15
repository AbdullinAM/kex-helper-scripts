import sys

from jcrashpack import *

jcrashpack_path = sys.argv[1]
benchmark = sys.argv[2]


crashes = read_crashes(jcrashpack_path)
description = crashes[benchmark]
class_path = get_class_path(jcrashpack_path, description["application"], description["version"])
trace_file = get_trace(jcrashpack_path, description["application"], description["id"])

print(class_path)
print(trace_file)
