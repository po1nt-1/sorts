import os
import json
import sys
import inspect

import gen
import sort


class my_error(Exception):
    pass


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


def read(file_name, folder_name):
    path = os.path.join(get_script_dir(), folder_name, file_name)

    if folder_name != "sorted_lists" and folder_name != "generated_lists":
        raise my_error("Что-то не так")

    if not os.path.exists(path):
        raise my_error("Папка с файлом не существует")

    data = []
    try:
        with open(path, 'r', encoding="utf-8") as f:
            data = json.load(f)
    except json.decoder.JSONDecodeError:
        raise my_error("Ошибка чтения файла")

    if not isinstance(data, list):
        raise my_error("Ошибка чтения файла")

    return data


def write(data, gen_mode=None, sort_mode=None):
    '''
    "increasing", "descending", "random", "recurring", "partially"\n
    "merge", "tim"
    '''
    if gen_mode is None and sort_mode is None:
        raise my_error("Что-то не так")
    if gen_mode is not None and sort_mode is not None:
        raise my_error("Что-то не так")

    if gen_mode is not None:
        path = os.path.join(get_script_dir(), "generated_lists")
    elif sort_mode is not None:
        path = os.path.join(get_script_dir(), "sorted_lists")

    if not os.path.exists(path):
        os.mkdir(path)

    gen_modes = ["increasing", "descending",
                 "random", "recurring", "partially"]

    if gen_mode in gen_modes:
        path_to_file = path + f"/{gen_mode}_{len(data)}"
        with open(path_to_file, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return
    elif gen_mode is None:
        pass
    else:
        raise my_error("Не поддерживаемый режим генерации")

    sort_modes = ["merge", "tim"]

    if sort_mode in sort_modes:
        path_to_file = path + f"/{len(data)}_{sort_mode}sorted"
        with open(path_to_file, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return
    elif sort_mode is None:
        pass
    else:
        raise my_error("Не поддерживаемый режим сортировки")


def get_file_list():
    path = os.path.join(get_script_dir(), "generated_lists")

    if not os.path.exists(path):
        raise my_error("Папка generated_lists не существует")

    return os.listdir(path)


if __name__ == "__main__":
    pass
