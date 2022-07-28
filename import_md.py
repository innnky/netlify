import os
from pathlib import Path
import time
filelist = []
with open("_sidebar.md","w") as f:
    def get_creation_time(path):
        return os.stat(path).st_birthtime
    def getctime(p):
        return time.strftime("%Y.%m.%d  &nbsp;&nbsp; %H: %M: %S", time.localtime(get_creation_time(str(p))))
    def getmtime(p):
        return time.strftime("%Y.%m.%d  &nbsp;&nbsp; %H: %M: %S", time.localtime(os.path.getmtime(str(p))))
    def scan(dirname,suffix):
        my_file = Path(dirname)
        for path in my_file.iterdir():
            if path.name.startswith("."):
                continue
            if path.name.endswith(".md") and not path.name.endswith("fail.md"):
                print("{}- [{}]({})".format(suffix,path.name[:-3],str(path)[:-3]), file=f)
                filelist.append((getctime(path),path.name[:-3],getmtime(path),path))
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


    print("- [最近发表](creat_time.md)", file=f)
    scan("docs", '')
    print("- 杂项", file=f)

    scan("docs/杂项", '  ')
    filelist.sort(reverse=True)
    with open("creat_time.md", "w") as c:
        c.write("""
 |            文章标题            |            创建时间             | 最后修改时间 |
| :----------------------------: |:---------------------------:| :----------: |
""")
        for item in filelist:
            c.write("|[{}]({})|{}|{}|\n".format(item[1], item[3], item[0], item[2]))
    print(filelist)