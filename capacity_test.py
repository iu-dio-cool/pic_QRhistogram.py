# 编写人员：刘嘉豪
#
# 开发时间：2023/5/20 9:01

# 先监测不同二维码阅读函数

from PIL import Image, ImageDraw
from pyzbar import pyzbar


def detect_qr_code(image_path):
    # 打开图像
    image = Image.open(image_path)

    # 转换为灰度图像
    gray = image.convert("L")

    # 使用 pyzbar 库识别二维码
    qr_codes = pyzbar.decode(gray)

    # 判断是否识别到二维码
    if qr_codes:
        # 遍历识别到的二维码
        for qr_code in qr_codes:
            # 提取二维码的边界框坐标
            (x, y, w, h) = qr_code.rect

            # 绘制边界框
            draw = ImageDraw.Draw(image)
            draw.rectangle([x, y, x + w, y + h], outline="green")

            # 解码二维码数据
            data = qr_code.data.decode("utf-8")
            print("识别到的二维码数据:", data)
    else:
        # 未识别到二维码
        print("未识别到二维码")

def capacity_test( ):





    # 调用函数进行二维码识别
    image_path = "D:\ALL_aboutSWU\IDEA_and_code\QR_codePic\\v1_M.png"  # 替换为你的二维码图像路径
    detect_qr_code(image_path)
