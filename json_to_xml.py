# encoding: utf-8
# @author: Evan/Hongji-Lin
# @file: json_to_xml.py
# @time: 2022/12/8 下午4:07
# @desc: 在最后的主函数处修改三个地方即可
import numpy as np
import json


# 读取json 标签内容
# 当中有2种模式:
# 一种rectangle，表示json文件是通过labelme的rectangle方式标注，
# 一种polygon，表示json文件是通过labelme的polygon方式标注。根据实际情况进行变换。

# step1
class ReadAnno:
    def __init__(self, json_path, process_mode="rectangle"):
        self.json_data = json.load(open(json_path))
        self.filename = self.json_data['imagePath']
        self.width = self.json_data['imageWidth']
        self.height = self.json_data['imageHeight']

        self.coordis = []
        assert process_mode in ["rectangle", "polygon"]
        if process_mode == "rectangle":
            self.process_polygon_shapes()
        elif process_mode == "polygon":
            self.process_polygon_shapes()

    def process_rectangle_shapes(self):
        for single_shape in self.json_data['shapes']:
            bbox_class = single_shape['label']
            xmin = single_shape['points'][0][0]
            ymin = single_shape['points'][0][1]
            xmax = single_shape['points'][1][0]
            ymax = single_shape['points'][1][1]
            self.coordis.append([xmin, ymin, xmax, ymax, bbox_class])

    def process_polygon_shapes(self):
        for single_shape in self.json_data['shapes']:
            bbox_class = single_shape['label']
            temp_points = []
            for couple_point in single_shape['points']:
                x = float(couple_point[0])
                y = float(couple_point[1])
                temp_points.append([x, y])
            temp_points = np.array(temp_points)
            xmin, ymin = temp_points.min(axis=0)
            xmax, ymax = temp_points.max(axis=0)
            self.coordis.append([xmin, ymin, xmax, ymax, bbox_class])

    def get_width_height(self):
        return self.width, self.height

    def get_filename(self):
        return self.filename

    def get_coordis(self):
        return self.coordis


# step2
from xml.dom.minidom import Document


#  创建labelimg标注格式的xml文件标签  并添加读取的数据，进行转换
class CreateAnno:
    def __init__(self, ):
        self.doc = Document()  # 创建DOM文档对象
        self.anno = self.doc.createElement('annotation')  # 创建根元素
        self.doc.appendChild(self.anno)

        self.add_folder()
        self.add_path()
        self.add_source()
        self.add_segmented()

        # self.add_filename()
        # self.add_pic_size(width_text_str=str(width), height_text_str=str(height), depth_text_str=str(depth))

    def add_folder(self, floder_text_str='JPEGImages'):
        floder = self.doc.createElement('floder')  ##建立自己的开头
        floder_text = self.doc.createTextNode(floder_text_str)  ##建立自己的文本信息
        floder.appendChild(floder_text)  ##自己的内容
        self.anno.appendChild(floder)

    def add_filename(self, filename_text_str='00000.jpg'):
        filename = self.doc.createElement('filename')
        filename_text = self.doc.createTextNode(filename_text_str)
        filename.appendChild(filename_text)
        self.anno.appendChild(filename)

    def add_path(self, path_text_str="None"):
        path = self.doc.createElement('path')
        path_text = self.doc.createTextNode(path_text_str)
        path.appendChild(path_text)
        self.anno.appendChild(path)

    def add_source(self, database_text_str="Unknow"):
        source = self.doc.createElement('source')
        database = self.doc.createElement('database')
        database_text = self.doc.createTextNode(database_text_str)  # 元素内容写入
        database.appendChild(database_text)
        source.appendChild(database)
        self.anno.appendChild(source)

    def add_pic_size(self, width_text_str="0", height_text_str="0", depth_text_str="3"):
        size = self.doc.createElement('size')
        width = self.doc.createElement('width')
        width_text = self.doc.createTextNode(width_text_str)  # 元素内容写入
        width.appendChild(width_text)
        size.appendChild(width)

        height = self.doc.createElement('height')
        height_text = self.doc.createTextNode(height_text_str)
        height.appendChild(height_text)
        size.appendChild(height)

        depth = self.doc.createElement('depth')
        depth_text = self.doc.createTextNode(depth_text_str)
        depth.appendChild(depth_text)
        size.appendChild(depth)

        self.anno.appendChild(size)

    def add_segmented(self, segmented_text_str="0"):
        segmented = self.doc.createElement('segmented')
        segmented_text = self.doc.createTextNode(segmented_text_str)
        segmented.appendChild(segmented_text)
        self.anno.appendChild(segmented)

    def add_object(self,
                   name_text_str="None",
                   xmin_text_str="0",
                   ymin_text_str="0",
                   xmax_text_str="0",
                   ymax_text_str="0",
                   pose_text_str="Unspecified",
                   truncated_text_str="0",
                   difficult_text_str="0"):
        object = self.doc.createElement('object')
        name = self.doc.createElement('name')
        name_text = self.doc.createTextNode(name_text_str)
        name.appendChild(name_text)
        object.appendChild(name)

        pose = self.doc.createElement('pose')
        pose_text = self.doc.createTextNode(pose_text_str)
        pose.appendChild(pose_text)
        object.appendChild(pose)

        truncated = self.doc.createElement('truncated')
        truncated_text = self.doc.createTextNode(truncated_text_str)
        truncated.appendChild(truncated_text)
        object.appendChild(truncated)

        difficult = self.doc.createElement('difficult')
        difficult_text = self.doc.createTextNode(difficult_text_str)
        difficult.appendChild(difficult_text)
        object.appendChild(difficult)

        bndbox = self.doc.createElement('bndbox')
        xmin = self.doc.createElement('xmin')
        xmin_text = self.doc.createTextNode(xmin_text_str)
        xmin.appendChild(xmin_text)
        bndbox.appendChild(xmin)

        ymin = self.doc.createElement('ymin')
        ymin_text = self.doc.createTextNode(ymin_text_str)
        ymin.appendChild(ymin_text)
        bndbox.appendChild(ymin)

        xmax = self.doc.createElement('xmax')
        xmax_text = self.doc.createTextNode(xmax_text_str)
        xmax.appendChild(xmax_text)
        bndbox.appendChild(xmax)

        ymax = self.doc.createElement('ymax')
        ymax_text = self.doc.createTextNode(ymax_text_str)
        ymax.appendChild(ymax_text)
        bndbox.appendChild(ymax)
        object.appendChild(bndbox)

        self.anno.appendChild(object)

    def get_anno(self):
        return self.anno

    def get_doc(self):
        return self.doc

    def save_doc(self, save_path):
        with open(save_path, "w") as f:
            self.doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')


# 更改参数运行: json格式文件所在的文件夹，将要保存的xml文件夹，以及原数据的标注方式。
# step3
import os
from tqdm import tqdm


# from read_json_anno import ReadAnno
# from create_xml_anno import CreateAnno


def json_transform_xml(json_path, xml_path, process_mode="rectangle"):
    json_path = json_path
    json_anno = ReadAnno(json_path, process_mode=process_mode)
    width, height = json_anno.get_width_height()
    filename = json_anno.get_filename()
    coordis = json_anno.get_coordis()

    xml_anno = CreateAnno()
    xml_anno.add_filename(filename)
    xml_anno.add_pic_size(width_text_str=str(width), height_text_str=str(height), depth_text_str=str(3))
    for xmin, ymin, xmax, ymax, label in coordis:
        xml_anno.add_object(name_text_str=str(label),
                            xmin_text_str=str(int(xmin)),
                            ymin_text_str=str(int(ymin)),
                            xmax_text_str=str(int(xmax)),
                            ymax_text_str=str(int(ymax)))
    xml_anno.save_doc(xml_path)


if __name__ == "__main__":
    root_json_dir = '/data/VOCdevkit/json'           # 根据自己的json文件地址需要
    root_save_xml_dir = '/data/VOCdevkit/xml'           # 根据自己要保存的xml文件地址修改
    for json_filename in tqdm(os.listdir(root_json_dir)):
        json_path = os.path.join(root_json_dir, json_filename)
        save_xml_path = os.path.join(root_save_xml_dir, json_filename.replace(".json", ".xml"))
        json_transform_xml(json_path, save_xml_path, process_mode="rectangle")   # 根据自己标注的模式修改


