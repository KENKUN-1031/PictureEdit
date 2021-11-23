# coding: UTF-8
from PIL import Image, ImageEnhance
import os

#ファイルを読み込んでる
img1 = Image.open('image1.jpg')

#pngにするとファイルサイズがちっちゃくなる
#img1.save('image1.png')

#写真を表示する
# img1.show()

#写真のサイズの変更
# max_size = (250,250)
# img1.thumbnail(max_size)
# img1.save('image1small.jpg')


#自動で'jpg'で終わるファイルを全て名前はそのままで'png'ファイルに変換する
# path = os.getcwd()
# for item in os.listdir(path):
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename,extension = os.path.splitext(item)
#         img1.save(filename+".png")


enhancer = ImageEnhance.Color(img1)
im1_enhance = enhancer.enhance(1.5)
im1_enhance.save('new_imag1.jpg', quality=95)

