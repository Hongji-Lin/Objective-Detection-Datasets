# encoding: utf-8
# @author: Evan/Hongji-Lin
# @file: xml_to_voc.py
# @time: 2022/12/8 下午4:58
# @desc: xml2voc 制作voc数据集

import os
import random

# ==================可能需要修改的地方=====================================#
root_path = "/home/lhj/Documents/GitHub/yolov5/data/VOCdevkit/VOC2022/"
xmlfilepath = "/home/lhj/Documents/GitHub/yolov5/data/VOCdevkit/VOC2022/Annotations/"  # 标注文件存放路径
saveBasePath = "/home/lhj/Documents/GitHub/yolov5/data/VOCdevkit/VOC2022/ImageSets/Main/"  # ImageSets信息生成路径
trainval_percent = 0.90
train_percent = 0.90
# ==================可能需要修改的地方=====================================#

os.chdir(root_path)
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
xml_list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(xml_list, tv)
train = random.sample(trainval, tr)

print("train and val size", tv)
print("train  size", tr)
ftrainval = open(saveBasePath + "trainval.txt", "w")
ftest = open(saveBasePath + "test.txt", "w")
ftrain = open(saveBasePath + "train.txt", "w")
fval = open(saveBasePath + "val.txt", "w")

for i in xml_list:
    name = total_xml[i][:-4] + "\n"
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()


