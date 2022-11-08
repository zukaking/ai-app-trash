#https://qiita.com/fleming_tone/items/be34de3f988bb2f0ab54
# -*- coding: utf-8 -*-
import numpy as np

import os
import cv2
import sys
import pathlib
import glob
from scipy.signal import qspline1d, qspline1d_eval, qspline2d,cspline2d

print("start")

if len(sys.argv) != 8:
    print("python test.py inputdir outputdir color luminance CLAHE noise revers")
    sys.exit()
else:   
    print("ok")
    input_path = sys.argv[1]
    file_list = glob.glob(input_path + "\\**.jpg", recursive=True)
    print(input_path)
    print(file_list)
    for item in file_list:
        split_name = item.split('\\')
        output_name = sys.argv[2] + "\\" + split_name[-2] + "\\" + split_name[-1]
        output_dir = sys.argv[2] + "\\" + split_name[-2]
        pathlib.Path(output_dir).mkdir(parents=True,exist_ok=True)
        if sys.argv[3] == "1":
            print("color")
            img = cv2.imread(item)          
        else:
            img = cv2.imread(item, cv2.IMREAD_GRAYSCALE)
        #img = cv2.imread(item, cv2.IMREAD_UNCHANGED)  # read image
        #img = cv2.imread(sys.argv[1])https://qiita.com/yoya/items/a11085f90f555b887cf6
        #img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        #img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        #img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        #cv2.imshow('equalize', img)
        #cv2.waitKey(0)

        #����������ʬ
        ###�����ε��٤�夲��
        #print(img)
        if sys.argv[4] == "1":
            chg_img=img*1.2 #���٤����ܤˤʤ�


        ###�����Υꥵ����
        height = img.shape[0]
        #img.shape[0]*0.5�Ǥ�Ȥ�Ⱦʬ�Υ�����
        width = img.shape[1]
        chg_img = cv2.resize(img , (int(width), int(height)))
        if sys.argv[5] == "1" and sys.argv[3] != "1":
            ###CLAHE�ʥҥ��ȥ���ब�Ǥ�����������˥Х餱��褦�˺���ʬ��
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            chg_img = clahe.apply(img)
        if sys.argv[6] == "1":
            ###�Υ���
            if sys.argv[3] == "1":
                row,col,ch = img.shape
            else:
                row,col = img.shape
            
            # ��
            pts_x = np.random.randint(0, col-1 , 1000) #0����(col-1)�ޤǤ��������ĺ��
            pts_y = np.random.randint(0, row-1 , 1000)
            img[(pts_y,pts_x)] = (255) #y,x�ν��֤ˤʤ뤳�Ȥ����

            # ��
            pts_x = np.random.randint(0, col-1 , 1000)
            pts_y = np.random.randint(0, row-1 , 1000)
            img[(pts_y,pts_x)] = (0)
        if sys.argv[7] == "1":
            ###�������Ĥ��
            chg_img = cv2.flip(img, 1) #��ʿ������ȿž
            chg_img = cv2.flip(img, 0) #��ľ������ȿž
            #print("end")

        print(output_name)
        cv2.imwrite(output_name,chg_img )  #write image
    print("end")