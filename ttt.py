# 编写人员：刘嘉豪
#
# 开发时间：2023/4/27 18:47
from PIL import Image
# from pyzbar.pyzbar import decode
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

def modify_qrcode_image(image_path, secret_data, image_save_path):
    # 读取图像
    image = Image.open(image_path)

    # 将图像转换为灰度图
    image_gray = image.convert('L')
    width = image.size[0]
    height = image.size[1]
    count = 0
    le = len(secret_data)
    secret_data_list = list(secret_data)
    for h in range(0, height):
        if count == le:
            break
        for w in range(0, width):
            if count == le:
                break
            pixel1 = image_gray.getpixel((w, h))
            if pixel1 == 0:
                if secret_data_list[count] == '1':
                    pixel1 = 200
                    image.putpixel((w, h), pixel1)
            if pixel1 == 255:
                if secret_data_list[count] == '1':
                    pixel1 = pixel1-200
                    image.putpixel((w, h), pixel1)
            count += 1


    # 保存修改后的图片
    image.save(image_save_path)

    # 返回修改后的图片路径
    return image_save_path
image_path = 'D:\ALL_aboutSWU\IDEA_and_code\QR_codePic\\v3_M.png'  # 待处理的图像路径
image_save_path = 'D:\ALL_aboutSWU\IDEA_and_code\QR_codePic_Output\\v3_M_out.png'
secret_data = '11'

modify_qrcode_image(image_path, secret_data, image_save_path)

image = Image.open(image_save_path)
image_gray = image.convert('L')
pixel_values = np.array(image_gray).ravel()
print(type(pixel_values),pixel_values)