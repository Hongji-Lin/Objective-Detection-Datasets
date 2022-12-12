# Objective-Detection-Datasets
目标检测数据集制作:VOC,COCO,YOLO等常用数据集格式的制作和互相转换脚本
demo/目录提供的原始的voc格式的20张原图和对应20个.xml标注．
下面的脚本都可以通过这个demo数据跑通.

# 制作自己VOC数据集（xml）
1、修改图片文件名字，统一修改成000001.jpg的命名格式
2、通过labelme标注数据获得json文件（如果是用labelimage标注的话直接获得xml文件）
3、将json文件转化成xml文件 (json_to_xml.py）
4、按照voc数据集格式将文件放入相应的位置

# 制作YOLOv5的数据集（txt）
1、先将数据集按照voc的格式放好（详情参考‘制作自己VOC数据集’）
2、将voc格式转变为yolo的格式（voc_to_yolo）

# 制作COCO数据集（json）
1、先将数据集按照voc的格式放好（详情参考‘制作自己VOC数据集’）
2、将voc格式转变为coco格式（voc_to_coco_v1）

<=========================================================================>

# json_to_xml.py
该脚本用于将labelme标注的json文件转换成xml文件

# xml_to_voc.py
该脚本用于将生成Images/Main中的信息

# voc_to_yolo.py 
一般先用这个
该脚本用于将voc格式转换成yolo格式（此时就已经划分验证集和训练集了）

## voc_to_yoloV5.py　和 voc_to_yoloV3.py
两个脚本实现的功能几乎相同,灵活取用
> - V5脚本实现将voc格式的数据转化为yoloV5需要的.txt标注文件,运行该脚本，会在voc/目录下生成
worktxt/目录(yolo需要的格式).
> - V3这个脚本除了生成.txt的标注(同上)，还会生成一个trianval.txt的索引,以前的yolov3系列用的多一点

## voc_to_coco_V1.py　和　voc_to_coco_V2.py
这两个脚本都是实现从voc的.xml标注格式转换到coco的.json格式,只是有所区别
> - v1版本实现了转换的同时进行训练／验证的分割
> - v2版本包含了segemetation字段(当训练htc等需要分割的任务时候网络需要用到)

# voc_split_train_val.py
该脚本用于生成voc/目录下的ImageSets/..目录,分割了训练和验证集

## coco_split_trainVal.py
该脚本实现coco格式的数据分割出训练集和验证集,同时里面还实现了一个去除背景图的方法(没有标注框的图)，可以结合上面的
voc_to_coco_v2.py使用.

## make_voc.py(其余各种格式转voc)
前面没有写coco转voc格式的脚本,make_voc.py就提供了一个制作voc格式数据的通用套路（核心代码）.