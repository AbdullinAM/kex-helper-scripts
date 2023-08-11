#!/bin/python3

import sys
import subprocess
import json
import os
import shutil

from juge11 import BENCHMARK_CLASSES
from juge11 import collections_classpath
from juge11 import jsoup_classpath
from juge11 import spatial4j_classpath
from juge11 import threeten_extra_classpath
from juge11 import ta4j_classpath

juge_path = sys.argv[1]

mode = "concolic"
name = "org.ta4j.core.criteria.SqnCriterion"

def print_benchmark(project_name: str, klass_name: str, mode_name: str, output_directory: str):
    classpath = ""
    if project_name == "COLLECTIONS":
        classpath = collections_classpath(juge_path)
    elif project_name == "JSOUP":
        classpath = jsoup_classpath(juge_path)
    elif project_name == "SPATIAL4J":
        classpath = spatial4j_classpath(juge_path)
    elif project_name == "THREETEN-EXTRA":
        classpath = threeten_extra_classpath(juge_path)
    elif project_name == "TA4J":
        classpath = ta4j_classpath(juge_path)
    print("--classpath {} --target {} --mode {} --output {}".format(classpath, klass_name, mode_name, output_directory))

for (index, benchmark) in enumerate(BENCHMARK_CLASSES):
    (project, klass) = benchmark
    if klass != name: 
    	continue
    output_dir = os.path.join("temp/", project.lower())
    print_benchmark(project, klass, mode, output_dir)
