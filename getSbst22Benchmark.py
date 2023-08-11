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
name = "com.google.common.collect.TreeRangeMap"

def print_benchmark(project_name: str, klass_name: str, mode_name: str, output_directory: str):
    classpath = ""
    if project_name == "FASTJSON":
        classpath = fastjson_classpath(juge_path)
    elif project_name == "GUAVA":
        classpath = guava_classpath(juge_path)
    elif project_name == "SEATA":
        classpath = seata_classpath(juge_path)
    elif project_name == "SPOON":
        classpath = spoon_classpath(juge_path)
    print("--classpath {} --target {} --mode {} --output {}".format(classpath, klass_name, mode_name, output_directory))

for (index, benchmark) in enumerate(BENCHMARK_CLASSES):
    (project, klass) = benchmark
    if klass != name: 
    	continue
    output_dir = os.path.join("temp/", project.lower())
    print_benchmark(project, klass, mode, output_dir)
