# 编写人员：刘嘉豪
#
# 开发时间：2023/4/7 20:43

import cv2
import numpy as np


# 定义Arnold映射
def arnold_map(x, y, n):

    for i in range(n):
        x, y = (x + y) % n, (x + 2 * y) % n
    return x, y


# 医学图像加密
def encrypt(img):
    # 将像素灰度值转换为二进制数列
    bin_img = np.unpackbits(img, axis=-1)
    # 对二进制数列进行Arnold映射
    n = img.shape[0]
    for i in range(n):
        for j in range(n):
            x, y = arnold_map(i, j, n)
            if x > i or y > j:
                bin_img[i][j], bin_img[x][y] = bin_img[x][y], bin_img[i][j]
    # 将二进制数列转换为像素灰度值
    enc_img = np.packbits(bin_img, axis=-1)
    print(enc_img.shape,enc_img.ndim,enc_img.size,n)
    # 进行误差扩散
    diff_matrix = np.array([[3, 7], [4, 6]])  # 扩散矩阵
    for i in range(n):
        for j in range(n):
            for k in range(3):
                enc_img[i][j][k] = (enc_img[i][j][k] * diff_matrix[i % 2][j % 2]) % 256

    return enc_img


# 医学图像解密
def decrypt(enc_img):
    # 将像素灰度值转换为二进制数列
    bin_enc_img = np.unpackbits(enc_img, axis=-1)
    n = enc_img.shape[0]
    # 进行误差扩散的逆过程
    diff_matrix_inv = np.array([[3, 7], [4, 6]])  # 扩散矩阵的逆矩阵
    # diff_matrix_inv = np.array([[2, 5], [1, 3]])  # 扩散矩阵的逆矩阵
    for i in range(n):
        for j in range(n):
            for k in range(3):
                bin_enc_img[i][j][k] = (bin_enc_img[i][j][k] * diff_matrix_inv[i % 2][j % 2]) % 256

    # 对二进制数列进行Arnold映射的逆过程
    for i in range(n):
        for j in range(n):
            x, y = arnold_map(i, j, n)
            if x > i or y > j:
                bin_enc_img[i][j], bin_enc_img[x][y] = bin_enc_img[x][y], bin_enc_img[i][j]

    # 将二进制数列转换为像素灰度值
    dec_img = np.packbits(bin_enc_img, axis=-1)

    return dec_img


if __name__ == '__main__':
    #img = cv2.imread('D:\\ALL_aboutSWU\\IDEA_and_code\\256_256\\Lena.png', cv2.IMREAD_GRAYSCALE)  # 加载医学图像
    img = cv2.imread('D:\\ALL_aboutSWU\\IDEA_and_code\\256_256\\Lena.png')
    enc_img = encrypt(img)  # 加密
    dec_img = decrypt(enc_img)  # 解密
    cv2.imshow('Original Image', img)
    cv2.imshow('Encrypted Image', enc_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
