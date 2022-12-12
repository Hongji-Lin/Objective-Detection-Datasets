# encoding: utf-8
# @author: Evan/Hongji-Lin
# @file: rename_file.py
# @time: 2022/12/12 上午10:06
# @desc:

import os


# 函数功能：批量修改文件夹路径下所有文件的文件名，在文件名前加数字7
def change_file_name(dir_path):
    files = os.listdir(dir_path)  # 读取文件名
    for i in files:
        # 设置旧文件名（路径+文件名）
        oldname = os.path.join(dir_path, i)
        # 设置新文件名
        newname = os.path.join(dir_path, '7' + i)
        # 用os模块中的rename方法对文件改名
        os.rename(oldname, newname)
        print(oldname, '======>', newname)


if __name__ == '__main__':
    change_file_name('data_plus')