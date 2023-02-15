import json
import os.path


def read_crashes(jcrashpack_path: str) -> dict:
    json_path = os.path.join(jcrashpack_path, "jcrashpack.json")
    crash_pack = json.loads(open(json_path).read())
    return crash_pack['crashes']


def get_class_path(jcrashpack_path: str, project: str, version: str) -> str:
    project_path = os.path.join(jcrashpack_path, "applications", project, version, "bin")
    jar_files = []
    for file in os.listdir(project_path):
        file_path = os.path.join(project_path, file)
        if os.path.isfile(file_path) and file_path.endswith(".jar"):
            jar_files.append(file_path)
    return ":".join(jar_files)


def get_trace(jcrashpack_path: str, project: str, crash_id: str) -> str:
    return os.path.join(jcrashpack_path, "crashes", project, crash_id, crash_id + ".log")
