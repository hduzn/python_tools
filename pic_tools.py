#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pic_tools.py
@Time    :   2021/03/10
@Author  :   HDUZN
@Version :   1.0
@Contact :   hduzn@vip.qq.com
@License :   (C)Copyright 2021-2022
@Desc    :   change_pic_size: 修改所有图片尺寸和dpi
             pic_to_pdf: 把所有图片合成成pdf, pdf_filename 是保存的pdf文件名
             pic_to_png: 图片转png格式, pic_type 参数可以设置需要转的图片格式
             代码中路径都是windows下路径，如果是linux系统，需要修改路径相关代码
'''

from PIL import Image
import os
import glob
import img2pdf
import shutil

def mkdir(path):
    outdir = os.path.exists(path)
    if not outdir:
        os.makedirs(path)

# 单张图片修改尺寸和dpi
def convertjpg(jpgfile, outdir, width, height, dpi_float):
    img = Image.open(jpgfile)
    # img.show()
    # print(img.mode)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        # print(new_img.mode)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)), dpi=(dpi_float,dpi_float))
    except Exception as e:
        print(e)

# 修改所有图片尺寸
def change_pic_size(path, width, height, dpi_float=72.0):
    path_files = path + '\\' + '*.*' # 需要修改的图片文件夹中所有图片文件
    out_dir = path + '_new' # 改好尺寸后的新文件夹
    mkdir(out_dir)
    path_list = glob.glob(path_files)
    # print(path_list)
    for jpgfile in path_list:
        convertjpg(jpgfile, out_dir, width, height, dpi_float)

# 把所有图片合成成pdf
def pic_to_pdf(picdir, pdf_filename):
    new_path = picdir + r'\*.*'
    print(new_path)
    new_path_list = glob.glob(new_path)
    with open(pdf_filename, 'wb') as f:
        f.write(img2pdf.convert(new_path_list))

# 图片转png格式
def pic_to_png(path, pic_type):
    outdir = path + pic_type
    mkdir(outdir)
    file_list = os.listdir(path)
    # print(file_list)
    for file in file_list:
        image = Image.open(path+'\\'+file)
        filename = os.path.splitext(file)[0]
        if(image.mode != 'RGB'):
            image = image.convert('RGB')
        image.save(outdir+'\\'+filename+'.'+pic_type)

# shutil.rmtree(outdir) # 删除文件夹

# 修改所有图片尺寸和dpi
change_pic_size(path=r'C:\Users\TOKEN\Desktop\六', width=2221, height=3142, dpi_float=72.0)

# 把所有图片合成成pdf
pic_to_pdf(picdir=r'C:\Users\TOKEN\Desktop\六_new', pdf_filename='六.pdf')

# 图片转png格式
pic_to_png(path=r'C:\Users\TOKEN\Desktop\六', pic_type='png')
