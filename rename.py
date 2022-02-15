# -- coding: utf-8 --
'''
@author:rushi
@version:1.0.0
@time:2022/1/26 20:14
python rename.py build
zip -q -r build.zip build
python rename.py src
'''
import re
import os
import sys
import pathlib

def renameCySo(file_path):
    p_file_path = pathlib.Path(file_path)
    # print(p_file_path)
    if p_file_path.exists():
        if p_file_path.is_file():
            pass
            # print(file_path,'是个文件')
        elif p_file_path.is_dir():
            # print(file_path, '是个目录')
            file_dirs = os.listdir(file_path)
            for f in file_dirs:
                old_src_name = file_path + '/' + f
                old_src_path = pathlib.Path(old_src_name)
                if old_src_path.is_file():
                    # print(old_src, '是个文件')
                    if re.search("\.so", f):
                        # print(f)
                        f_list = f.split('.')
                        if len(f_list) == 3:
                            new_name = f_list[0] + '.' + f_list[2]
                            new_src_name = file_path + '/' + new_name
                            print('重命名',old_src_name,new_src_name)
                            old_src_path.rename(new_src_name)
                            # os.rename(old_src, new_src)
                    elif re.search("\.c", f):
                        # 删除文件
                        old_src_path.unlink()
                        print('删除文件',old_src_name)
                elif old_src_path.is_dir():
                    pass
                    # print(old_src, '是个目录')
                    renameCySo(old_src_name)
        else:
            pass
            # print(file_path, '不是文件也不是目录')
    else:
        pass
        # print(file_path,'不存在')

if __name__ == '__main__':
    file_path = sys.argv[1]
    file_path = os.getcwd() + '/' + file_path
    renameCySo(file_path)