import os

from juge10 import BENCHMARK_CLASSES as BENCHMARK_CLASSES_10
from juge10 import fastjson_classpath
from juge10 import guava_classpath
from juge10 import seata_classpath
from juge10 import spoon_classpath

from juge11 import BENCHMARK_CLASSES as BENCHMARK_CLASSES_11
from juge11 import collections_classpath
from juge11 import jsoup_classpath
from juge11 import spatial4j_classpath
from juge11 import threeten_extra_classpath
from juge11 import ta4j_classpath

from juge12 import BENCHMARK_CLASSES as BENCHMARK_CLASSES_12
from juge12 import bytebuddy_classpath
from juge12 import errorprone_classpath
from juge12 import javapoet_classpath

def get_classpath_by_project(juge_path: str, project_name: str):
    classpath = ""
    if project_name == "FASTJSON":
        classpath = fastjson_classpath(juge_path)
    elif project_name == "GUAVA":
        classpath = guava_classpath(juge_path)
    elif project_name == "SEATA":
        classpath = seata_classpath(juge_path)
    elif project_name == "SPOON":
        classpath = spoon_classpath(juge_path)
    elif project_name == "COLLECTIONS":
        classpath = collections_classpath(juge_path)
    elif project_name == "JSOUP":
        classpath = jsoup_classpath(juge_path)
    elif project_name == "SPATIAL4J":
        classpath = spatial4j_classpath(juge_path)
    elif project_name == "TA4J":
        classpath = ta4j_classpath(juge_path)
    elif project_name == "THREETEN-EXTRA":
        classpath = threeten_extra_classpath(juge_path)
    elif project_name == "JSOUP":
        classpath = jsoup_classpath(juge_path)
    elif project_name == "BYTEBUDDY":
        classpath = bytebuddy_classpath(juge_path)
    elif project_name == "ERRORPRONE":
        classpath = errorprone_classpath(juge_path)
    elif project_name == "JAVAPOET":
        classpath = javapoet_classpath(juge_path)
    return classpath