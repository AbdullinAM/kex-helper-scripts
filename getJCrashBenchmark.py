import sys

from jcrashpack import *

jcrashpack_path = '/home/abdullin/workspace/JCrashPack'# sys.argv[1]
benchmark = 'MATH-100b' # sys.argv[2]
depth = 1


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
