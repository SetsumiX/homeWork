import threading
import os

def copy_file(src, dir):
    with open(src, "rb") as src_file:
        with open(dir, "wb") as dst_file:
            dst_file.write(src_file.read())


def copy_directory(src, dir):
    os.makedirs(dir, exist_ok=True)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dir, item)

        if os.path.isdir(src_path):
            copy_directory(src_path, dst_path)
        else:
            copy_file(src_path, dst_path)

thread_copy_dir = threading.Thread(target=copy_directory, args=(input('Введите путь откуда >>> '), input('Введите путь куда >>> ')))

thread_copy_dir.start()

thread_copy_dir.join()
