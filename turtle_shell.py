# 编写人员：刘嘉豪
#
# 开发时间：2023/5/29 15:18

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy.matlib import rand

np.set_printoptions(threshold=np.inf)


# 生成一个龟背矩阵.参数是龟壳大小 !! 上下是X轴，左右是Y轴
def Make_turtmat(row, col):
    # np.zeros((10, 15))构建的上下是X轴，左右是Y轴
    turtmat = np.zeros((row, col))
    turtmat[0, 0] = 6
    # 第一列
    for j in range(1, col):
        turtmat[0, j] = np.mod(turtmat[0, j - 1] + 1, 8)

    # 第2-col行
    for i in range(1, row):
        if np.mod(i, 2) == 0:
            turtmat[i, :] = np.mod(turtmat[i - 1, :] - 3, 8)
        else:
            turtmat[i, :] = np.mod(turtmat[i - 1, :] - 2, 8)
    # print(turtmat) #设置断点可看
    return turtmat


# 找到相关符合位置,返回值是新的像素对 !! 上下是X轴，左右是Y轴
def Find_Pos(X, Y, tortoise, number, ):
    width = len(tortoise)
    height = len(tortoise[0])
    # 对边界进行特殊处理
    if ((X == 0 and Y == 0) or (X == width and Y == 0) or (X == 0 and Y == height) or (X == width and Y == height) or
            (X == 0 and Y % 2 == 0) or (X == width and Y % 2 == 0) or
            (Y == 0 and (X % 4 == 0 or X % 4 == 3)) or (Y == height and (X % 4 == 2 or Y % 4 == 1))):
        print('该点在边界上    ')
        if X == 0 and Y == 0:  # 判断其是否是龟壳矩阵的左上顶点
            X1, Y1, X2, Y2 = matrix(X, Y, number, tortoise)
            temp1, temp2 = X1, Y1
            if (X2 - X) ** 2 + (Y2 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
                temp1, temp2 = X2, Y2
            X, Y = temp1, temp2
        elif X == width and Y == 0:  # 判断其是否是龟壳矩阵的左下顶点
            X1, Y1, X2, Y2 = matrix(X - 2, Y, number, tortoise)
            temp1, temp2 = X1, Y1
            if (X2 - X) ** 2 + (Y2 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
                temp1, temp2 = X2, Y2
            X, Y = temp1, temp2
        elif X == 0 and Y == height:  # 判断其是否是龟壳矩阵的右上顶点
            X1, Y1, X2, Y2 = matrix(X, Y - 2, number, tortoise)
            temp1, temp2 = X1, Y1
            if (X2 - X) ** 2 + (Y2 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
                temp1, temp2 = X2, Y2
            X, Y = temp1, temp2
        elif X == width and Y == height:  # 判断其是否是龟壳矩阵的右下顶点
            X1, Y1, X2, Y2 = matrix(X - 2, Y - 2, number, tortoise)
            temp1, temp2 = X1, Y1
            if (X2 - X) ** 2 + (Y2 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
                temp1, temp2 = X2, Y2
            X, Y = temp1, temp2
        elif X == 0 and Y % 2 == 0:  # 判断其是否在龟壳矩阵上边界、是否需要边界处理
            X1, Y1, X2, Y2 = matrix(X, Y - 1, number, tortoise)
            temp1, temp2 = X1, Y1
            if (X2 - X) ** 2 + (Y2 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
                temp1, temp2 = X2, Y2
            X, Y = temp1, temp2
        elif X == width and Y % 2 == 0:  # 判断其是否在龟壳矩阵下边界、是否需要边界处理
            X1, Y1, X2, Y2 = matrix(X - 2, Y - 1, number, tortoise)
            temp1, temp2 = X1, Y1
            if (X2 - X) ** 2 + (Y2 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
                temp1, temp2 = X2, Y2
            X, Y = temp1, temp2
        elif Y == 0 and (X % 4 == 0 or X % 4 == 3):  # 判断其是否在龟壳矩阵左边界、是否需要边界处理
            X1, Y1, X2, Y2 = matrix(X - 1, Y, number, tortoise)
            temp1, temp2 = X1, Y1
            if (X2 - X) ** 2 + (Y2 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
                temp1, temp2 = X2, Y2
            X, Y = temp1, temp2
        elif Y == height and (X % 4 == 2 or X % 4 == 1):  # 判断其是否在龟壳矩阵右边界、是否需要边界处理
            X1, Y1, X2, Y2 = matrix(X - 1, Y - 2, number, tortoise)
            temp1, temp2 = X1, Y1
            if (X2 - X) ** 2 + (Y2 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
                temp1, temp2 = X2, Y2
            X, Y = temp1, temp2

        return X, Y

    # 判断其是否是龟壳内部两点中的上内部点
    if ((tortoise[X, Y] == 1 and tortoise[X + 1, Y] == 6) or (tortoise[X, Y] == 3 and tortoise[X + 1, Y] == 0) or
            (tortoise[X, Y] == 5 and tortoise[X + 1, Y] == 2) or (tortoise[X, Y] == 7 and tortoise[X + 1, Y] == 4)):
        print('该点在龟壳上内    ')
        X, Y = traversal(X - 1, Y, number, tortoise)
        return X, Y

    # 判断其是否是龟壳内部两点中的下内部点
    if ((tortoise[X, Y] == 6 and tortoise[X - 1, Y] == 1) or (tortoise[X, Y] == 0 and tortoise[X - 1, Y] == 3) or
            (tortoise[X, Y] == 2 and tortoise[X - 1, Y] == 5) or (tortoise[X, Y] == 4 and tortoise[X - 1, Y] == 7)):
        print('该点在龟壳下内    ')
        X, Y = traversal(X - 2, Y, number, tortoise)
        return X, Y

    # 剩下的点全在龟壳的边上，且只有上下顶点两类
    if tortoise[X, Y] % 2 == 1:  # 判断其是否在龟壳边的上顶点
        print('该点在龟壳上边    ')
        X1, Y1 = traversal(X, Y, number, tortoise)
        X2, Y2 = traversal(X - 2, Y - 1, number, tortoise)
        X3, Y3 = traversal(X - 2, Y + 1, number, tortoise)
        temp1, temp2 = X1, Y1
        if (X2 - X) ** 2 + (Y2 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
            temp1, temp2 = X2, Y2
        if (X3 - X) ** 2 + (Y3 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
            temp1, temp2 = X3, Y3
        X, Y = temp1, temp2
        return X, Y

    if tortoise[X, Y] % 2 == 0:  # 判断其是否在龟壳边的下顶点
        print('该点在龟壳下顶边    ')
        X1, Y1 = traversal(X - 3, Y, number, tortoise)
        X2, Y2 = traversal(X - 1, Y - 1, number, tortoise)
        X3, Y3 = traversal(X - 1, Y + 1, number, tortoise)
        temp1, temp2 = X1, Y1
        if (X2 - X) ** 2 + (Y2 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
            temp1, temp2 = X2, Y2
        if (X3 - X) ** 2 + (Y3 - Y) ** 2 < (temp1 - X) ** 2 + (temp2 - Y) ** 2:
            temp1, temp2 = X3, Y3
        X, Y = temp1, temp2
        return X, Y


# 在此定义函数 traversal() 和 matrix()
# traversal() 函数从上顶点开始遍历一个龟壳，并返回需要寻找点的坐标
def traversal(X, Y, number, tortoise):
    if (X > 255 or X + 1 < 1 or X + 2 < 1 or X + 2 > 256 or X + 3 < 1 or X + 3 > 256 or
            Y < 1 or Y > 256 or Y - 1 < 1 or Y - 1 > 256 or Y + 1 < 1 or Y + 1 > 256):
        X = float('inf')
        Y = float('inf')
    elif tortoise[X, Y] == number:
        pass
    elif tortoise[X + 1, Y] == number:
        X = X + 1
    elif tortoise[X + 1, Y - 1] == number:
        X = X + 1
        Y = Y - 1
    elif tortoise[X + 1, Y + 1] == number:
        X = X + 1
        Y = Y + 1
    elif tortoise[X + 2, Y] == number:
        X = X + 2
    elif tortoise[X + 2, Y - 1] == number:
        X = X + 2
        Y = Y - 1
    elif tortoise[X + 2, Y + 1] == number:
        X = X + 2
        Y = Y + 1
    elif tortoise[X + 3, Y] == number:
        X = X + 3
    return X, Y


# 分别从左上顶点和右下顶点开始，遍历一个3*3矩阵，并返回需要寻找点的坐标
# 分别从左上顶点和右下顶点开始遍历的作用是找出距离最小的点
def matrix(X1, Y1, number, tortoise):
    flag = 0
    X2 = X1
    Y2 = Y1

    for i in range(3):
        for j in range(3):
            if tortoise[X1 + i, Y1 + j] == number:
                X1 = X1 + i
                Y1 = Y1 + j
                flag = 1
                break
        if flag == 1:
            break

    flag = 0
    for i in range(2, -1, -1):
        for j in range(2, -1, -1):
            if tortoise[X2 + i, Y2 + j] == number:
                X2 = X2 + i
                Y2 = Y2 + j
                flag = 1
                break
        if flag == 1:
            break

    return X1, Y1, X2, Y2


# 嵌入函数
def Turtle_Shell_dataHiding(image_path, secret_data):
    # 读取图像
    image = Image.open(image_path)
    # 将图像转换为灰度图
    image_gray = image.convert('L')
    # 获取图像像素值
    pixel_values = np.array(image_gray)
    # 获取图像长 宽
    width, height = image.size
    if len(secret_data) > len(pixel_values):
        return False
    stego_pixel_values = np.copy(pixel_values)
    shifted_pixel_values = stego_pixel_values.flatten()  # shifted_pixel_values用来放修改后的像素 数组
    shifted_pixel_values2 = stego_pixel_values.flatten()  # shifted_pixel_values2一对一对的取出来操作

    turtle_matrix = Make_turtmat(width, height)  # 图片256*256 龟壳也用256*256
    for i in range(len(secret_data)):
        shifted_pixel_values[2 * i], shifted_pixel_values[2 * i + 1] = \
            Find_Pos(shifted_pixel_values2[2 * i], shifted_pixel_values2[2 * i + 1], turtle_matrix, secret_data[i])
        print("原始坐标", shifted_pixel_values2[2 * i], shifted_pixel_values2[2 * i + 1], "新坐标", \
              shifted_pixel_values[2 * i], shifted_pixel_values[2 * i + 1], "secret_data", secret_data[i], \
              "之前值", turtle_matrix[shifted_pixel_values2[2 * i], shifted_pixel_values2[2 * i + 1]], "之后值",
              turtle_matrix[shifted_pixel_values[2 * i], shifted_pixel_values[2 * i + 1]])
    shifted_pixel_values = shifted_pixel_values.reshape((width, height))
    stego_image = Image.fromarray(shifted_pixel_values)

    return stego_image


# 提取过程 data_len数据长度
def Turtle_Shell_dataExtract(stegoimage_path, data_len):
    # 读取图像
    # image = Image.open(image_path)
    # 将图像转换为灰度图
    # image_gray = image.convert('L')
    # 获取图像像素值
    pixel_values = np.array(stegoimage_path)
    # 获取图像长 宽
    width, height = stegoimage_path.size
    if data_len > len(pixel_values):
        return False
    turtle_matrix = Make_turtmat(width, height)
    stego_pixel_values = np.copy(pixel_values)
    shifted_pixel_values = stego_pixel_values.flatten()
    data = ''
    for i in range(data_len):
        data += str(turtle_matrix[shifted_pixel_values[2*i], shifted_pixel_values[2*i + 1]])
        print(turtle_matrix[shifted_pixel_values[2*i], shifted_pixel_values[2*i + 1]])
    print(data)


# image_path = 'D:\ALL_aboutSWU\IDEA_and_code\little_pic.png'
image_path = 'D:\ALL_aboutSWU\IDEA_and_code\\256_256\Lena.png'  # 待处理的图像路径
s_data = np.random.randint(0, 8, 5)  # 随机生成0-8字符串

Stego = Turtle_Shell_dataHiding(image_path, s_data)
Turtle_Shell_dataExtract(Stego, len(s_data))
print("secret data:", s_data)
# 显示载体图像
plt.subplot(2, 2, 1)
plt.imshow(Image.open(image_path), cmap='gray')
plt.title('Original Image')
# 显示隐藏后的图像
plt.subplot(2, 2, 2)
plt.imshow(Stego, cmap='gray')
plt.title('Stego Image')
plt.waitforbuttonpress()
