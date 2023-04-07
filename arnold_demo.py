import cv2
import numpy as np
import Substitution_Error_RateValue
from PIL import Image

# 定义 Arnold 置乱函数
def arnold_shuffle(img, key):
    # 获取图像的宽度和高度
    width, height = img.shape[:2]
    # 初始化置乱后的图像
    shuffled_img = np.zeros_like(img)

    # 获取置乱算法所需的参数
    a, b, = key

    # 对每个像素进行置乱
    for x in range(width):
        for y in range(height):
            new_x = (1 * x + b * y) % width
            new_y = (a * x + (a * b + 1) * y) % height
            shuffled_img[new_x, new_y] = img[x, y]

    return shuffled_img


def more_arnold_shuffle(img, num_shuffle, key):
    imge = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    # 多次置乱
    for i in range(num_shuffle):
        # 对图像进行置乱
        imge = arnold_shuffle(imge, key)
    return imge


# 读取要置乱的图像
# img = cv2.imread('./512_512/lena.png', cv2.IMREAD_GRAYSCALE)
# 单次置乱
# 获取置乱算法所需的参数
# a, b= key
# img = arnold_shuffle(img,key=(1,1))

# 多次置乱
img = more_arnold_shuffle('./512_512/lena.png', 3, key=(1, 1))
im = Image.fromarray(img)
im.save('test.png')
Substitution_Error_RateValue.Ser_Value('./512_512/lena.png','test.png')
Substitution_Error_RateValue.Ser_Value('./512_512/lena.png','./512_512/Output1/Lena_EMD_k_4_n_2.png')
print(Substitution_Error_RateValue.image_entropy('./512_512/lena.png'))
print(Substitution_Error_RateValue.image_entropy('test.png'))
print('实验后数据'+str(Substitution_Error_RateValue.image_entropy('./512_512/Output1/Lena_EMD_k_4_n_2.png')))
# 显示置乱后的图像
# cv2.imshow('Shuffled Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
