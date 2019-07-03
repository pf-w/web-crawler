#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-08  15:37

import pytesseract
from PIL import Image

image = Image.open('pic/d.png')

vcode = pytesseract.image_to_string(image)

print (vcode)