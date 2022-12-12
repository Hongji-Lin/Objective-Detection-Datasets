# encoding: utf-8
# @author: Evan/Hongji-Lin
# @file: csv_to_voc.py
# @time: 2022/12/12 上午10:51
# @desc:

# encoding=utf-8
import os
from collections import defaultdict
import csv
import cv2
import ipdb
import misc_utils as utils  # pip3 install utils-misc==0.0.5 -i https://pypi.douban.com/simple/
import json

utils.color_print('建立JPEGImages目录', 3)
os.makedirs('Annotations', exist_ok=True)
utils.color_print('建立Annotations目录', 3)
os.makedirs('ImageSets/Main', exist_ok=True)
utils.color_print('建立ImageSets/Main目录', 3)

files = os.listdir('train')
files.sort()

mem = defaultdict(list)

confirm = input('即将生成annotations，大约需要3-5分钟，是否开始(y/n)? ')
if confirm.lower() != 'y':
    utils.color_print(f'Aborted.', 3)
    exit()

with open('train.csv', 'r') as f:
    csv_file = csv.reader(f)
    '''
    读取的csv_file是一个iterator，每个元素代表一行
    '''
    for i, line in enumerate(csv_file):
        if i == 0:
            continue
        filename, width, height, bbox, _ = line
        x1, y1, x2, y2 = json.loads(bbox)
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        x2 += x1
        y2 += y1
        mem[filename].append([x1, y1, x2, y2])

for i, filename in enumerate(mem):
    utils.progress_bar(i, len(mem), 'handling...')
    img = cv2.imread(os.path.join('train', filename))
    # height, width, _ = img.shape

    with open(os.path.join('Annotations', filename.rstrip('.jpg')) + '.xml', 'w') as f:
        f.write(f"""<annotation>
    <folder>train</folder>
    <filename>{filename}.jpg</filename>
    <size>
        <width>1024</width>
        <height>1024</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>\n""")
        for x1, y1, x2, y2 in mem[filename]:
            f.write(f"""    <object>
        <name>wheat</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>{x1}</xmin>
            <ymin>{y1}</ymin>
            <xmax>{x2}</xmax>
            <ymax>{y2}</ymax>
        </bndbox>
    </object>\n""")
        f.write("</annotation>")

files = list(mem.keys())
files.sort()
f1 = open('ImageSets/Main/train.txt', 'w')
f2 = open('ImageSets/Main/val.txt', 'w')
train_count = 0
val_count = 0

with open('ImageSets/Main/all.txt', 'w') as f:
    for filename in files:
        # filename = filename.rstrip('.jpg')
        f.writelines(filename + '\n')

        if utils.gambling(0.1):  # 10%的验证集
            f2.writelines(filename + '\n')
            val_count += 1
        else:
            f1.writelines(filename + '\n')
            train_count += 1

f1.close()
f2.close()

utils.color_print(f'随机划分 训练集: {train_count}张图，测试集：{val_count}张图', 3)
