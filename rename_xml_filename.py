# encoding: utf-8
# @author: Evan/Hongji-Lin
# @file: rename_xml_filename.py
# @time: 2022/12/13 下午5:31
# @desc:

# import os
# from xml.etree.ElementTree import parse, Element
# out_dir = '/home/lhj/Documents/GitHub/Objective-Detection-Datasets/data/rename_xml/'  # 这里是保存的目标文件夹
# b = os.listdir('/home/lhj/Documents/GitHub/Objective-Detection-Datasets/data/json/')
# for i in b:
#     print(i)
#     dom = parse('/home/lhj/Documents/GitHub/Objective-Detection-Datasets/data/json/'+i)
#     root = dom.getroot()
#     print(root)
#     for obj in root.iter('/home/lhj/Documents/GitHub/Objective-Detection-Datasets/data/json'):
#         obj.find('filename').text = i.rstrip(".xml")+".jpg"
#         name1 = obj.find('filename').text
#         print(name1)
#     dom.write(out_dir+"Gray_"+i, xml_declaration=True)
#      # “Gray是我自己定义的，可以改为任意值，i为原来的名字，也可以直接修改成想要的名字”


import os
import shutil
import xml.etree.ElementTree as ET


def change_xml(xml_path, xml_new_path, image_savepath):  # 转换标签函数
    # 1.打开xml文档，并解析树
    tree = ET.parse(xml_path)  # 将xml解析为树
    root = tree.getroot()  # 获取根节点

    # 2.修改filename和path
    filename = root.find('filename')
    path = root.find('path')

    filename.text = image_savepath.split('\\')[-1]
    path.text = image_savepath

    # 3.调用树的方法write()保存更新XML文件（以UTF-8的格式保存）
    tree.write(xml_new_path, 'UTF-8')


def change_imagename_xml(image_dir, xml_dir, image_savedir, xml_savedir, extra='img_'):
    """
    实现将image_dir中的图像重命名并保存到新的文件夹，并且同步更改xml_dir中的xml文件中的filename、path为图像的新名字和新路径
    :param image_dir: 存放原始图像文件夹
    :param xml_dir: 存放原始xml文件夹
    :param image_savedir: 存放新名字图像的文件
    :param xml_savedir: 存放新的xml文件
    :param extra: 新图像名称改为extra+序号，例如extra默认为'img_'，则新名称为：img_1.jpg
    """
    assert os.path.exists(image_dir), f'\"{image_dir}\" not exists. change over!'
    assert os.path.exists(xml_dir), f'\"{xml_dir}\" not exists. change over!'

    if not os.path.exists(image_savedir):
        os.makedirs(image_savedir)
    if not os.path.exists(xml_savedir):
        os.makedirs(xml_savedir)

    filelist = os.listdir(image_dir)

    for i, file in enumerate(filelist):
        filename, ext = os.path.splitext(file)
        new_filename = extra + str(i)

        # change image name and copy
        image_savepath = os.path.join(image_savedir, new_filename + ext)
        shutil.copy(os.path.join(image_dir, file), image_savepath)

        # change xml's filename and path -> save in new dir
        xml_path = os.path.join(xml_dir, filename + '.xml')
        xml_new_path = os.path.join(xml_savedir, new_filename + '.xml')
        change_xml(xml_path, xml_new_path, image_savepath)


if __name__ == '__main__':
    image_dir = '/data1/imgs'
    xml_dir = '/data1/xml'

    image_savedir = '/home/lhj/Documents/GitHub/Objective-Detection-Datasets/data/rename_imgs'
    xml_savedir = '/home/lhj/Documents/GitHub/Objective-Detection-Datasets/data/rename_xml'
    change_imagename_xml(image_dir, xml_dir, image_savedir, xml_savedir)
