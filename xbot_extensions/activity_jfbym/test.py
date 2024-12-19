import xbot
import xbot_visual
import os
import xbot_visual
import base64
import json
import base64
import io
import urllib
import http.client
from PIL import ImageGrab, Image
import os
import ssl
import http.client
import urllib.parse
from PIL import Image
from io import BytesIO
from ctypes import windll
from xbot.web.element import WebElement
from xbot import print, sleep, web




def main(args):
    # test_download_image()
    #   relative_to='window'
    web_page = web.get_active(mode='chrome')
    x, y, width, height = web_page.find("图片_dy").get_bounding(relative_to='window')
    print(x,y,width,height)
