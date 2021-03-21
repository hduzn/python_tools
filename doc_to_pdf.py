#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 安装工具包:pip install docx2pdf
from docx2pdf import convert
from win32com import client
import os

'''
# file_list = get_filelist(path, [])
def get_filelist(dir, file_list):
    newDir = dir
    if os.path.isfile(dir):
        file_list.append(dir)
        # # 若只是要返回文件文，使用这个
        # file_list.append(os.path.basename(dir))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # #if s == "xxx":
               #continue
            newDir=os.path.join(dir,s)
            get_filelist(newDir, file_list)
    return file_list
'''
def get_filelist(path):
    file_list = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            if(filename.startswith('~$')):
                continue
            else:
                # 文件名列表，包含完整路径
                file_list.append(os.path.join(home, filename))
                # 文件名列表，只包含文件名
                # file_list.append(filename)
    return file_list

def doc2docx(doc_file):
    word = client.Dispatch("Word.Application")
    doc = word.Documents.Open(doc_file)
    doc.SaveAs("{}x".format(doc_file), 12)
    doc.Close()
    word.Quit()
    return doc_file+'x'

# 批量转换
def doc_to_pdf():
    # 文件位置
    path = r'C:\小现代化(1)'

    file_list = get_filelist(path)
    # print(file_list)

    # 定义空list,存放文件列表
    docx_files = []
    for file in file_list:
        if(file.endswith(".docx")):
            docx_files.append(file)
        elif(file.endswith(".doc")):
            docx_file = doc2docx(file)
            docx_files.append(docx_file)
    # print(docx_files)
    for docx in docx_files:
        print(docx)
    print('docx文件数：', len(docx_files))

    # 转换文件
    print('-----------------开始转换 docx 文件-----------------')
    for file in docx_files:
        print(file)
        #print(file.split('.docx')[0]+'.pdf')
        convert(file,file.split('.docx')[0]+'.pdf')
        #print(file+'转换成功')

print('-----------------开始转换-----------------')
doc_to_pdf()
print('-----------------转换完成！-----------------')
