
import matplotlib.pyplot as plt
from PIL import Image

def get_gray_pix(img):
    pix=[]
    width, hight = get_w_h(img)
    img = Image.open(img).convert("L")

    for i in range(hight):
        for j in range(width):
            pix.append(img.getpixel((j,i)))
    return pix

def get_w_h(img):
    img=Image.open(img)
    width=img.width
    hight=img.height
    return width,hight
def generate_hist(data,bin):
    histogram, bins, patch = plt.hist(data, bin,
                                      facecolor='blue', histtype='stepfilled')  # histograming

    return histogram
def Find_min_Distancce(list,seek_num,flag_num,Critical_flag):#第一个是列表，第二是需要寻找的数，第三个是指定的参考数字,第四个为参考数字
    Distance=256#先预设一个最大的距离
    for i in range(0,len(list)):
        if list[i]==seek_num:
            flag=i+1#这个是0点的下标
            if flag_num<Critical_flag:
                if abs(flag_num-flag)<Distance and (flag<flag_num or (flag>flag_num and flag<Critical_flag)):#比较得出最近的距离
                    Distance=abs(flag_num-flag)
                    flag_min=flag#保存一下当前距离的下标
            else:
                if abs(flag_num-flag)<Distance and (flag>flag_num or (flag<flag_num and flag>Critical_flag)):#比较得出最近的距离
                    Distance=abs(flag_num-flag)
                    flag_min=flag#保存一下当前距离的下标
    return flag_min

def pic_histogram_key_inf(pic_address,show_histogram):

    #函数说明：用来将图片转换成直方图，并且返回直方图当中的像素数量最多的位置和次多的位置，以及返回离最高和次高位置的0点位置
    #形参数说明：pic_address图片地址   show_histogram为1显示直方图为0不显示
    #返回参数说明：MaxPix最多像素的个数,MaxPoint个数最多的像素值,To_MaxPoint_min_Point离个数最多的像素值最近的零点像素
    #           Second_MaxPix次多像素的个数,Second_MaxPoint个数次多的像素值,To_SecondMaxPoint_min_Point离个数次多的像素值最近的零点像素

    cover_pix = get_gray_pix(pic_address)  # 获取图像的像素值
    width, hight = get_w_h(pic_address)  # 获取图片的行数列数
    numberBins = [i + 0.5 for i in list(range(0, 256))]  # 设置条状的范围
    histogram = generate_hist(cover_pix, numberBins)  # 产生直方图
    if show_histogram==1:
        plt.show()  # 展示直方图
    histogram_list = histogram.tolist()  # 转换成列表方便操作 这个列表里面存储的是0到255像素的个数
    histogram_list_smalltobig = sorted(histogram_list)  # 对列表进行从小到大的排序
    MaxPix=histogram_list_smalltobig[-1]
    Second_MaxPix=histogram_list_smalltobig[-2]
    MaxPoint = histogram_list.index(MaxPix) + 1  # 获取最多数量像素的下标
    Second_MaxPoint = histogram_list.index(Second_MaxPix) + 1  # 获取第二多数量像素的下标
    # 下面寻找离最多个数下标最近的像素
    To_MaxPoint_min_Point = Find_min_Distancce(histogram_list, 0.0, MaxPoint,Second_MaxPoint)
    # 下面寻找离次多个数下标最近的像素
    To_SecondMaxPoint_min_Point = Find_min_Distancce(histogram_list, 0.0, Second_MaxPoint,MaxPoint)
    return MaxPix,MaxPoint,To_MaxPoint_min_Point,Second_MaxPix,Second_MaxPoint,To_SecondMaxPoint_min_Point

# if __name__ == '__main__':
#
#     MaxPix,MaxPoint,To_MaxPoint_min_Point,Second_MaxPix,Second_MaxPoint,To_SecondMaxPoint_min_Point=pic_histogram_key_inf("./11.jpg",1)
#     print(MaxPix,MaxPoint,To_MaxPoint_min_Point,Second_MaxPix,Second_MaxPoint,To_SecondMaxPoint_min_Point)




