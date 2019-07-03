#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-08  16:43

"""
    Python Imaging Library (PIL)

    使用pytesseract之前先安装tesseracr-orc并配置环境变量

    pytesseract.pytesseract.tesseract_cmd
    = r"D:\Tesseract\tesseract-ocr\tesseract.exe"    # 指定tesseract的路径

    image = Image.open('file_path')

     pytesseract.image_to_string(image, lang)
     # 若识别中文简体则指定lang=ch_sim，需要下载对用语言包，放入D:\Tesseract\tesseract-ocr\tessdata中
     # 其中中文的包是：chi_sim.traineddata，
     # 语言包下载路径：https://github.com/tesseract-ocr/tesseract/wiki/Data-Files
"""

import pytesseract
from PIL import Image

# 指定tesseract的路径
# pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract\tesseract-ocr\tesseract.exe"

image_0 = Image.open('pic/b.png')

verification_code = pytesseract.image_to_string(image_0)

print(verification_code)

print()

# 识别中文
image_1 = Image.open('pic/chi_sim_2.png')

VCode = pytesseract.image_to_string(image_1, lang='chi_sim')

print(VCode)
