#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   orc_tool.py
@Time    :   2021/03/13
@Author  :   HDUZN
@Version :   1.0
@Contact :   hduzn@vip.qq.com
@License :   (C)Copyright 2021-2022
@Desc    :   pic_ocr：本地单张图片文字识别
             url_pic_ocr：网络图片文字识别
             笔记：http://i007it.com/2021/03/13/Python%E5%AF%B9%E5%9B%BE%E7%89%87%E8%BF%9B%E8%A1%8C%E6%96%87%E5%AD%97%E8%AF%86%E5%88%AB/
'''

# here put the import lib
from aip import AipOcr

# 读取图片
def get_file_content(pic_file):
    with open(pic_file, 'rb') as f:
        return f.read()

# 本地单张图片文字识别
def pic_ocr(pic_file):
    app_id = '2******0'
    app_key = '6E*************************a'
    secret_key = 'z2*************************3'

    client = AipOcr(app_id, app_key, secret_key)

    image = get_file_content(pic_file)

    # 调用 通用文字识别（高精度版），提取图片中的文字内容
    text = client.basicAccurate(image)

    result = text['words_result']
    # print(result)
    for line in result:
        print(line['words'])

# 网络图片文字识别
def url_pic_ocr(pic_url):
    app_id = '2******0'
    app_key = '6E*************************a'
    secret_key = 'z2*************************3'

    client = AipOcr(app_id, app_key, secret_key)

    # 调用 通用文字识别（含位置信息版），提取图片中的文字内容
    text = client.generalUrl(pic_url)

    result = text['words_result']
    # print(result)
    for line in result:
        print(line['words'])

# 本地单张图片文字识别
pic_ocr('ocr_test.jpg') # 路径也可以用绝对路径

# 网络图片文字识别
url_pic_ocr(r'http://n.sinaimg.cn/henan/transform/20160114/6sMt-fxnrahr8267165.jpg')
