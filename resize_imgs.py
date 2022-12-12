# encoding: utf-8
# @author: Evan/Hongji-Lin
# @file: resize_imgs.py
# @time: 2022/12/12 上午10:03
# @desc:

import cv2
import os

os.mkdir(r"data_plus") #创建新文件夹
path = 'work/voc_data/JPEGImages/' #原图像路径
save_path = 'data_plus/'  # 修改后的图像路径
files = os.listdir(path)

for file in files:
    img = cv2.imread(path + "/" + file)
    # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 转化为灰度图
    try:
        img = cv2.resize(img,(640,640))
        cv2.imwrite(save_path+"/"+str(file),img)
    except:
        continue