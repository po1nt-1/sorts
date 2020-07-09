import os
import json


def get_script_dir(follow_symlinks=True) -> str:
    '''получить директорию со скриптом'''

    # https://clck.ru/P8NUA
    if getattr(sys, 'frozen', False):  # type: ignore
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def read(mode):
    pass


def write(data, mode):
    if mode == "increasing":
        pass
    if mode == "descending":
        pass
    if mode == "random":
        pass
    if mode == "recurring":
        pass
    if mode == "partially":
        pass
    else:
        raise Exception("Не поддерживаемый тип последовательности")

    path = os.path.join(get_script_dir(), "lists")
    path_to_file = path + f"/{mode}_{len(data)}"

    with open(path_to_file, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
