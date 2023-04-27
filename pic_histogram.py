from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from qrcode_HS import plot_image_histogram

def histogram_shift_hide(image_path, secret_data, shift):
    """
    直方图平移的可逆信息隐藏算法

    参数：
    image_path (str)：待处理的图像路径
    secret_data (str)：要隐藏的秘密数据
    shift (int)：直方图平移的位移量

    返回值：
    stego_image (PIL.Image.Image)：隐藏秘密数据后的图像
    extracted_data (str)：提取出的秘密数据
    """

    # 读取图像
    image = Image.open(image_path)

    # 将图像转换为灰度图
    image_gray = image.convert('L')

    # 获取图像像素值
    pixel_values = np.array(image_gray)

    # 对图像进行直方图平移
    shifted_pixel_values = (pixel_values + shift) % 256

    # 将秘密数据隐藏到图像中
    binary_secret_data = ''.join(format(ord(char), '08b') for char in secret_data)
    num_pixels_needed = len(binary_secret_data)
    stego_pixel_values = np.copy(shifted_pixel_values)

    for i in range(num_pixels_needed):
        row = i // image_gray.width
        col = i % image_gray.width
        stego_pixel_values[row][col] = (shifted_pixel_values[row][col] & 254) | int(binary_secret_data[i])

    # 创建隐藏秘密数据后的图像
    stego_image = Image.fromarray(stego_pixel_values)
    stego_image.save(image_save_path)
    # 提取隐藏的秘密数据
    extracted_data = ''
    for i in range(num_pixels_needed):
        row = i // image_gray.width
        col = i % image_gray.width
        extracted_data += str(stego_pixel_values[row][col] & 1)

    extracted_data = ''.join([chr(int(extracted_data[i:i+8], 2)) for i in range(0, len(extracted_data), 8)])

    return stego_image, extracted_data

# 测试示例
image_path = 'D:\ALL_aboutSWU\IDEA_and_code\QR_codePic\\v3_M.png'  # 待处理的图像路径
image_save_path ='D:\ALL_aboutSWU\IDEA_and_code\QR_codePic_Output\\v3_M_out.png'
secret_data = 'Hello, world!'  # 要隐藏的秘密数据
shift = 0  # 直方图平移的位移量

# 进行信息隐藏
stego_image, extracted_data = histogram_shift_hide(image_path, secret_data, shift)
Original_ImageHS = plot_image_histogram(image_path)
Stego_ImageHS = plot_image_histogram(image_save_path)

# 显示原始图像
plt.subplot(2, 2, 1)
plt.imshow(Image.open(image_path), cmap='gray')
plt.title('Original Image')

# 显示隐藏秘密数据后的图像
plt.subplot(2, 2, 2)
plt.imshow(stego_image, cmap='gray')
plt.title('Stego Image')

# 显示原始图像直方图
plt.subplot(2, 2, 3)
plt.imshow(Original_ImageHS, cmap='gray')
plt.title('Original_ImageHS')

# 显示隐藏秘密数据后的直方图
plt.subplot(2, 2, 4)
plt.imshow(stego_image, cmap='gray')
plt.title('Stego_ImageHS')
plt.show()

# 打印提取出的秘密数据
print('Extracted Data:', extracted_data)
