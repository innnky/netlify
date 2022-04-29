import os
from pathlib import Path
with open("_sidebar.md","w") as f:

    def scan(dirname,suffix):
        my_file = Path(dirname)
        for path in my_file.iterdir():
            if path.name.startswith("."):
                continue
            if path.name.endswith(".md"):
                print("{}- [{}]({})".format(suffix,path.name[:-3],str(path)[:-3]), file=f)
            if path.is_dir():
                if path.name == "杂项":
                    continue
                print("{}- {}".format(suffix,path.name), file=f)
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
                if path.name == "杂项":
                    continue
                scan_s(str(path), suffix+"  ")
            # print(os.path.isfile(file),end=" ")
            # print(suffix+file)


    print("- [首页](/)", file=f)
    scan("docs", '')
    print("- 杂项", file=f)

    scan("docs/杂项", '  ')