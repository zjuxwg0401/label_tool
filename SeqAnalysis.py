'''
本程序计算
- 平均绝对像素大小：
- 最大绝对像素大小：
- 最小绝对像素大小：
- 相对像素大小：

输入为一系列txt文件，每个文件中的数据格式为：x,y,w,h


'''

############################################ 须要修改的参数  #############################################
startframe = 0  #首帧index
endframe   = 250

#末帧index
width = 4096 #宽
height = 1800 #高
st_label_path_prefix = "/home/ubuntu/dataset1/zjuxjy0401/grassland/"                              #输出txt文件路径前缀
st_label_path_prefix = "/home/ubuntu/dataset1/zjuxjy0401/ST_Fusion_object_detection/data/p4_1/"   #输出txt文件路径前缀
st_label_path_prefix = "/Users/shallwego2/Pictures/seq7/st_label/"
st_label_path_prefix = "/Users/shallwego2/Pictures/seq10/st_label/"

########################################################################################################################
import numpy as np
import cv2, time
import os

####################################  读txt ############################################################

w_max = 0
w_min = 1000
h_max = 0
h_min = 1000
area_max = 0
area_min = 1000000
w_sum = 0
h_sum = 0
area_sum = 0

for frame_num in np.arange(startframe, endframe+1):
    st_label_name = st_label_path_prefix + "st_frame" + "{0:04d}".format(frame_num) + ".txt"

    with open(st_label_name) as f_label:
        st_label = f_label.readlines()
        annotations = []

        for j, annotation in enumerate(st_label):
            annotation = annotation.split()
            annotation = float(annotation[0]),float(annotation[1]),float(annotation[2]),float(annotation[3])
            x,y,w,h = np.array(annotation)
            area = w*h

            w_sum = w_sum + w
            h_sum = h_sum + h
            area_sum = area_sum + area

            if w > w_max:
                w_max = w
            if h > h_max:
                h_max = h
            if area > area_max:
                area_max = area

            if w < w_min:
                w_min = w
            if h < h_min:
                h_min = h
            if area < area_min:
                area_min = area

average_w = w_sum/(endframe+1)
average_h = h_sum/(endframe+1)
average_area = area_sum/(endframe+1)

print("w_max:{}".format(w_max))
print("w_min:{}".format(w_min))
print("h_max:{}".format(h_max))
print("h_min:{}".format(h_min))
print("area_max:{}".format(area_max))
print("abs_area_min:{}".format(area_min))
print("abs_average_w:{}".format(average_w))
print("abs_average_h:{}".format(average_h))
print("abs_average_area:{}".format(average_area))
print("relateive_average_w:{}".format(average_w/width))
print("relateive_average_h:{}".format(average_h/height))
print("relateive_average_area:{}".format(average_area/(width*height)))