# Objective-Detection-Datasets
 目标检测的数据集相关预处理

# 制作自己VOC数据集
1、修改图片文件名字，统一修改成000001.jpg的命名格式
2、通过labelme标注数据获得json文件（如果是用labelimage标注的话直接获得xml文件）
3、将json文件转化成xml文件 (json_to_xml.py）
4、按照voc数据集格式将文件放入相应的位置

# 制作YOLOv5的数据集
1、先将数据集按照voc的格式放好（详情参考‘制作自己VOC数据集’）
2、将voc格式转变为yolo的格式（voc_to_yolo）

# 制作COCO数据集
1、先将数据集按照voc的格式放好（详情参考‘制作自己VOC数据集’）
2、将voc格式转变为coco格式（voc_to_coco）