# encoding: utf-8
# @author: Evan/Hongji-Lin
# @file: rename_suffix.py
# @time: 2022/12/12 上午9:51
# @desc:


# 批量生成.jpg文件
import os
# file_dir 文件目录 old_suffix 原后缀 new_suffix 新后缀


def change_suffix(file_dir, old_suffix, new_suffix):
    for file_name in os.listdir(file_dir):
        # os.path.splitext 分割文件主名和后缀名
        split_file = os.path.splitext(file_name)
        # 获得文件后缀 split_file[0] 文件主名 split_file[1] 后缀名
        file_suffix = split_file[1]
        if old_suffix == file_suffix:
            new_file_name = split_file[0] + new_suffix
            # os.rename 重命名
            os.rename(os.path.join(file_dir, file_name), os.path.join(file_dir, new_file_name))


if __name__=='__main__':
    change_suffix('work/voc_data/JPEGImages', '.JPG', '.jpg')