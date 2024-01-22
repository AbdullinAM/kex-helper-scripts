#!/bin/python

import sys
import subprocess
import json
import os
import shutil

from paths import *
from juge_common import *

juge_path = JUGE_PATH
if len(sys.argv) > 1:
    jcrashpack_path = sys.argv[1]

mode = "concolic"
name = "com.alibaba.fastjson.serializer.BooleanCodec"

def print_benchmark(project_name: str, klass_name: str, mode_name: str, output_directory: str):
    classpath = get_classpath_by_project(juge_path, project_name)
    print("--classpath {} --target {} --mode {} --output {}".format(classpath, klass_name, mode_name, output_directory))

for (index, benchmark) in enumerate(BENCHMARK_CLASSES_10 + BENCHMARK_CLASSES_11):
    (project, klass) = benchmark
    if klass != name: 
    	continue
    output_dir = os.path.join("temp/", project.lower())
    print_benchmark(project, klass, mode, output_dir)
