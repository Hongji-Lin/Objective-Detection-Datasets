# encoding: utf-8
# @author: Evan/Hongji-Lin
# @file: rename_file.py
# @time: 2022/12/12 上午10:06
# @desc:

import os
import sys


# 函数功能：批量修改文件夹路径下所有文件的文件名，修改为00000x
def change_file_name(old_path, new_path):
    old_files = os.listdir(old_path)  # 读取文件名,待修改文件夹
    for i in range(0, len(old_files)):
        # 修改前的文件名
        print("修改前的文件名为：{}".format(old_files[i]))
        # 设置旧文件名（路径+文件名）
        oldname = os.path.join(old_path, old_files[i])
        # 设置新文件名
        newname = os.path.join(new_path, str(("%06d"%i))+'.'+'jpg')  # 文件重新命名,根据修改类型改变后缀
                                                                     # 如果想实现00000~99999，只需将这里的6改为5，诸如此类。
        # 用os模块中的rename方法对文件改名
        os.rename(oldname, newname)
        # 修改后的文件名
        print("修改后的文件名为：{}".format(str(("%06d"%i))+'.'+'jpg'))
        sys.stdin.flush()  # 更新


if __name__ == '__main__':
    # 温馨提示：old/new的地址可以是同个地址
    old_path = '/home/lhj/Documents/GitHub/Objective-Detection-Datasets/demo/imgs'
    new_path = '/home/lhj/Documents/GitHub/Objective-Detection-Datasets/demo/test1'
    change_file_name(old_path, old_path)


# 函数功能：同时批量修改图片和标签所有文件的文件名
# def change_file_name(imgs_path, labels_path):
#     imgs_files = os.listdir(imgs_path)       # 读取图片文件名
#     imgs_files.sort(key=lambda x: x.split('.')[0])
#     labels_files = os.listdir(labels_path)  # 读取标签文件名
#     labels_files.sort(key=lambda x: x.split('.')[0])
#     for i in range(0, len(imgs_files)):
#         # 修改前的文件名
#         print("修改前的图片文件名为：{}".format(imgs_files[i]))
#         print("修改前的标签文件名为：{}".format(labels_files[i]))
#         # 设置旧文件名（路径+文件名）
#         imgs_oldname = os.path.join(imgs_path, imgs_files[i])
#         labels_oldname = os.path.join(labels_path, labels_files[i])
#         # 设置新文件名
#         imgs_newname = os.path.join(imgs_path, str(("%06d"%i))+'.'+'jpg')
#         labels_newname = os.path.join(labels_path, str(("%06d"%i))+'.'+'json')
#         # 用os模块中的rename方法对文件改名
#         os.rename(imgs_oldname, imgs_newname)
#         os.rename(labels_oldname, labels_newname)
#         # 修改后的文件名
#         print("修改后的文件名为：{}".format(str(("%06d" % i)) + '.' + 'jpg'))
#         print("修改后的文件名为：{}".format(str(("%06d" % i)) + '.' + 'json'))
#         sys.stdin.flush()  # 更新
#
#
# if __name__ == '__main__':
#     imgs_path = '/home/lhj/Documents/GitHub/Objective-Detection-Datasets/demo/imgs1'
#     labels_path = '/home/lhj/Documents/GitHub/Objective-Detection-Datasets/demo/labels'
#     change_file_name(imgs_path, labels_path)



