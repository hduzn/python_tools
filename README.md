# python_tools

doc_to_pdf.py

批量Word文档转PDF格式文件。

- 1.get_filelist(path): 得到path路径下所有的文件(绝对路径)，除去~$开头的缓存文件;
- 2.doc2docx(doc_file): 把.doc文件转成.docx文件，因为 docx2pdf包只能处理 docx文件；
- 3.doc_to_pdf(): 批量转换成pdf

如果需要清除原有的doc/docx文件，直接在目录下搜索.doc，搜索出所有.doc/.docx文件后，全选删除，就只留下pdf文件了。

---------------------------------------------------------------------------------------------------
orc_tool.py

用百度的ORC识别的应用。已实现单张图片/单张网络图片的识别。

批量实现就遍历目录操作就行。

笔记看这里：
http://i007it.com/2021/03/13/Python%E5%AF%B9%E5%9B%BE%E7%89%87%E8%BF%9B%E8%A1%8C%E6%96%87%E5%AD%97%E8%AF%86%E5%88%AB/

---------------------------------------------------------------------------------------------------
pic_tools.py

- change_pic_size方法: 修改所有图片尺寸和dpi
- pic_to_pdf方法: 把所有图片合成成pdf, pdf_filename 是保存的pdf文件名
- pic_to_png方法: 图片转png格式, pic_type 参数可以设置需要转的图片格式

PS.代码中路径都是windows下路径，如果是linux系统，需要修改路径相关代码
