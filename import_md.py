import os
from pathlib import Path
def scan(dirname,suffix):
    my_file = Path(dirname)
    for path in my_file.iterdir():
        if path.name.startswith("."):
            continue
        if path.name.endswith(".md"):
            print("{}- [{}]({})".format(suffix,path.name[:-3],str(path)[:-3]))
        if path.is_dir():
            print("{}- {}".format(suffix,path.name))
            scan(str(path), suffix+"  ")
        # print(os.path.isfile(file),end=" ")
        # print(suffix+file)

def scan_s(dirname,suffix):
    my_file = Path(dirname)
    for path in my_file.iterdir():
        if path.name.startswith("."):
            continue
        if path.name.endswith(".md"):
            print('        "/{}",'.format(str(path)[:-3]))
        if path.is_dir():
            scan_s(str(path), suffix+"  ")
        # print(os.path.isfile(file),end=" ")
        # print(suffix+file)
scan_s("docs", '')