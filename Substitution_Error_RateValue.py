# 编写人员：刘嘉豪
#
# 开发时间：2023/3/27 11:08
import cv2
import numpy as np


def Ser_Value(original_image, stego_image):
    # 加载原始图像和隐藏信息后的图像
    original_image = cv2.imread(original_image, cv2.IMREAD_GRAYSCALE)
    stego_image = cv2.imread(stego_image, cv2.IMREAD_GRAYSCALE)
    # 计算像素差异
    diff = np.abs(original_image.astype(int) - stego_image.astype(int))

    # 计算 SER 值
    SER = np.count_nonzero(diff) / (original_image.shape[0] * original_image.shape[1])
    # 显示 SER 值
    print("SER:", SER)


def image_entropy(image_path):
    # 读取图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 计算像素值分布
    hist, _ = np.histogram(img, bins=np.arange(257))

    # 计算概率分布
    prob = hist / np.sum(hist)

    # 计算信息熵
    entropy = -np.sum(prob * np.log2(prob + 1e-7))

    return entropy

