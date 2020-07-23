from PIL import Image
import os

"""压缩图片到指定大小"""

#获取文件名
def getname(path):
    for file in os.walk(path):
        return file[2]

#文件路径
path = r"D:\Users\Administrator\Desktop\IMAGE\input\0"
names = getname(path)
#目标大小，MB
glob = 1
for name in names:
    file = path + "\\" + name
    size = os.path.getsize(file)
    while size > glob*1024*1024:
        im = Image.open(file)
        w, h = im.size
        #每次压缩90%
        new_w = int(w*0.9)
        new_h = int(h*0.9)
        simg = im.resize((new_w, new_h),Image.ANTIALIAS)
        simg.save(file)
        size = os.path.getsize(file)
print("done!")


