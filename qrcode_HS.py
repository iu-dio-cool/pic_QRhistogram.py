# 编写人员：刘嘉豪
# 基于hs直方图平移的二维码信息隐藏实验
# 开发时间：2023/4/16 16:25


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import io
np.set_printoptions(threshold=np.inf)

def plot_image_histogram(image_path):
    """
    读取图片，绘制直方图，并返回直方图图片
    :param image_path: 图片文件路径
    :return: 直方图图片
    """
    # 读取图像
    image = Image.open(image_path)

    # 将图像转换为灰度图
    image_gray = image.convert('L')

    # 获取图像像素值
    pixel_values = np.array(image_gray).ravel()
    # print(type(pixel_values),pixel_values)
    # 统计像素值的频次
    pixel_counts = np.bincount(pixel_values)

    # 绘制直方图
    plt.bar(range(256), pixel_counts)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Pixel Value Histogram')

    # 将绘制的直方图图片保存到内存中
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    histogram_image = Image.open(buffer)

    # 关闭绘图窗口
    plt.close()

    return histogram_image

# plot_image_histogram("D:\ALL_aboutSWU\IDEA_and_code\QR_codePic\\v3_M.png")
# plot_image_histogram("D:\ALL_aboutSWU\IDEA_and_code\QR_codePic_Output\\v3_M_out.png")