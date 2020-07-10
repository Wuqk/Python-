import tesserocr
from PIL import Image

def processing_image(image):
    img = image.convert('L')  #转化为灰度图
    pixdata = img.load()
    w, h = img.size
    threshold = 127  # 该阈值不适合所有验证码，具体阈值请根据验证码情况设置
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

#去噪点
def delete_spot(image):
    data = image.getdata()
    w, h = image.size
    black_point = 0
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            mid_pixel = data[w * y + x]  # 中央像素点像素值
            if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]
                # 判断上下左右的黑色像素点总个数
                if top_pixel < 100:
                    black_point += 1
                if left_pixel < 100:
                    black_point += 1
                if down_pixel < 100:
                    black_point += 1
                if right_pixel < 100:
                    black_point += 1
                if black_point < 1:
                    image.putpixel((x, y), 255)
                black_point = 0
    return image

image = Image.open(r'D:\Users\Administrator\Desktop\IMAGE\P1.jpg')
def chuli(image):
    im = delete_spot(processing_image(image))
    w1,h1 = im.size
    #对图片大小进行处理
    if w1<h1:
        i = im.resize((int(100),int(h1*(100/w1))))
    else:
        i = im.resize((int(w1*(100/h1)),int(100)))
    return i

#文字识别
print(tesserocr.image_to_text(chuli(image)))

