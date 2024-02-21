import numpy as np
import cv2 
import matplotlib.pyplot as plt
import os
import os.path as osp
import random

def rename_file(dir):
    for file in os.listdir(dir):
        old_name = osp.join(dir, file)
        new_name = osp.join(dir, file.replace('nolmal','normal'))
        os.rename(old_name,new_name)

def compute_coord(x,y,M):
    # 计算变换后的齐次坐标
    coords = np.dot(M, np.array([x, y, 1]))

    # 将齐次坐标转换为笛卡尔坐标
    x_prime, y_prime = coords[0] / coords[2], coords[1] / coords[2]
    return x_prime, y_prime





    # for _ in os.listdir(A):
    #     if _.endswith('JPG'):
    #         os.rename(osp.join(A, _),osp.join(A,_.replace('.JPG','.jpg')))
    




    # for filename in os.listdir(B):
    #     if osp.exists(osp.join(A, filename.replace('.png', '.jpg'))):
    #         i+=1
    #         h1,w1 = cv2.imread(osp.join(A, filename.replace('.png', '.jpg'))).shape[:2]
    #         img = cv2.imread(osp.join(B, filename))
    #         h2,w2 = img.shape[:2]
    #         if w1 ==w2 and h1==h2:
    #             j+=1
    #         else:
    #             # img = cv2.resize(img,(w1, h1))
    #             # cv2.imwrite(osp.join(B,filename),img)
    #             print(filename)
    # print(i)
    # print(j)








        # a = osp.join(A, file.split('_')[0]+'_nolmal.jpg')
        # b = osp.join(B, file)

        # # 读取两张图像  
        # img1 = cv2.imread(a)  
        # img2 = cv2.imread(b)  
        
        # # 获取图像尺寸  
        # height1, width1, channels1 = img1.shape[:3]  
        # height2, width2, channels2 = img2.shape[:3]  
        
        # # 判断尺寸是否相等  
        # if height1 == height2 and width1 == width2:  
        #     pass
        #     #print("两张图像的尺寸相等")  
        # else:  
        #     print(file, "两张图像的尺寸不相等")


#     # 定义矩阵
#     xx = np.zeros((256,256))
#     xx[100:150,100:150]=1
#     xx[10:15,10:15]=1
#     xx[10:20,2]=1
#     xx[...]*=255
#     xx = cv2.imread('fp.jpg', cv2.IMREAD_GRAYSCALE).astype(np.uint8) 

#     # # 计算矩形
#     # xx = xx.astype(np.uint8)
#     # #_, contours, _ = cv2.findContours(x, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     # x, y, w, h = cv2.boundingRect(xx)

#     # # 画出矩形
#     # img = np.zeros((256, 256, 3), dtype=np.uint8)
#     # cv2.rectangle(xx, (x, y), (x+w, y+h), (255, 255, 0), 2)

# # 定义结构元素（半径为3的圆形）  
# kernel = np.ones((5, 5), np.uint8)  
  
# # 腐蚀操作  
# eroded = cv2.erode(xx, kernel, iterations=2)  
  
# # 膨胀操作  
# dilated = cv2.dilate(eroded, kernel, iterations=2)  
  
# # 显示结果图像  
# cv2.imshow('Original', xx)  
# cv2.imshow('Dilated', dilated)  
# cv2.waitKey(0)  
# cv2.destroyAllWindows()

