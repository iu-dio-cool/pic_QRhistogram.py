# 编写人员：刘嘉豪
#
# 开发时间：2023/4/27 17:03
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from qrcode_HS import plot_image_histogram


def histogram_shift_hide(image_path, secret_data, image_Dpath):
    """
    直方图平移的可逆信息隐藏算法

    参数：
    image_path (str)：待处理的图像路径
    secret_data (str)：要隐藏的秘密数据
    image_Dpath (str):处理的图像路径存放地址

    返回值：

    """

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
        for w in range(0, width):
            if count == le:
                break
            pixel1 = image_gray.getpixel((w, h))
            if secret_data_list[count] == '1':
                if pixel1 == 0:
                    pixel1 += 1
                elif pixel1 == 255:
                    pixel1 -= 1
            count += 1
            image.putpixel((w, h), pixel1)
    image.save(image_Dpath)
    return image_Dpath


# 测试示例
image_path = 'D:\ALL_aboutSWU\IDEA_and_code\QR_codePic\\v3_M.png'  # 待处理的图像路径
image_save_path = 'D:\ALL_aboutSWU\IDEA_and_code\QR_codePic_Output\\v3_M_out.png'
secret_data = '111111011'  # 要隐藏的秘密数据

# 进行信息隐藏
histogram_shift_hide(image_path, secret_data, image_save_path)
Original_ImageHS = plot_image_histogram(image_path)
Stego_ImageHS = plot_image_histogram(image_save_path)

# 显示原始图像
plt.subplot(2, 2, 1)
plt.imshow(Image.open(image_path), cmap='gray')
plt.title('Original Image')

# 显示隐藏秘密数据后的图像
plt.subplot(2, 2, 2)
plt.imshow(Image.open(image_save_path))
# plt.imshow(image_save_path, cmap='gray')
plt.title('Stego Image')

# 显示原始图像直方图
plt.subplot(2, 2, 3)
plt.imshow(Original_ImageHS, cmap='gray')
plt.title('Original_ImageHS')

# 显示隐藏秘密数据后的直方图
plt.subplot(2, 2, 4)
plt.imshow(Stego_ImageHS, cmap='gray')
plt.title('Stego_ImageHS')
plt.show()
