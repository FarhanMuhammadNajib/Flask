import sys
sys.path.insert(0,'../Backend')
from colorMap import get_new_color_img

def CodeVisual(filePath):
    im = get_new_color_img(filePath)
    return im