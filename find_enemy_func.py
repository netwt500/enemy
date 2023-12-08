import cv2
import numpy as np

def extract_red(img):
    #70  74 202
    mask1 = (img[:,:,0] >= 68) & (img[:,:,0] <= 80) & \
           (img[:,:,1] >= 71) & (img[:,:,1] <= 77) & \
           (img[:,:,2] >= 180) & (img[:,:,2] <= 210)

    mask2 = (img[:,:,0] >= 46) & (img[:,:,0] <= 63) & \
           (img[:,:,1] >= 53) & (img[:,:,1] <= 75) & \
           (img[:,:,2] >= 112) & (img[:,:,2] <= 120)

    img[:, :, :] = [255, 255, 255]
    img[mask1] = [0, 0, 0]
    img[mask2] = [0, 0, 0]

    return img

def image_read(name):
    img = cv2.imread(name)
    extract = extract_red(img)
    gray = cv2.cvtColor(extract, cv2.COLOR_BGR2GRAY)
    return img, extract, gray

def invertAndDilate(gray):
    # 글자의 경계를 팽창시켜 두껍게 만듦
    invert = 255 - gray
    kernel = np.ones((3, 3), np.uint8)
    invert = cv2.dilate(invert, kernel=kernel, iterations=3)
    return invert

def find_Contours(img):

    # 안에 모든 카운너 박스를 찾는다
    contours, h = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours




x2 = 500 #메인 이미지 픽셀값 단. 정사각형이여야 작동이 잘됨
y2 = 500



# return은 두개를 반환한다 하나는 img 하나는 output인데 top에 사람이 있으면 0 미드에 있으면 1 바텀에 있으면 2
def contours(img, contours):

    OUTPUT = []

    for index, c in enumerate(contours):

        x_center = 0 #찾아진 카우너 x 중앙
        y_center = 0 #찾아진 카우너 y 중앙

        for xy in c:
            x_center += xy[0][0] / len(c)
            y_center += xy[0][1] / len(c)

        if len(c) < 30:
            pass
        else:
            if x2 / 3.5 > x_center and y2 / 3.5 < y_center or x2 / 12 > y_center and y2 / 12 > x_center:
                pass
            else:
                cv2.drawContours(img, contours[index], -1, (0, 255, 0), 2)
                cv2.circle(img, center=(int(x_center), int(y_center)), radius=10, color=(255, 0, 0), thickness=-1)

                if(x_center < x2 / 4.7 or y_center < y2 / 4.7 ):
                    OUTPUT.append(0)
                    #print("TOP")
                if(y_center > -1 * x_center + x2 - (x2 / 9.6) and y_center < -1 * x_center + x2 + (x2 / 9.6)):
                    OUTPUT.append(1)
                    #print("middle")
                if(x_center > x2 / 4.7 * 3.7 or x_center > y2 / 4.7 * 3.7):
                    OUTPUT.append(2)
                    #print("bottom")

    return img, OUTPUT






"""
img, ex_red, grayed_img = image_read('qwer.png')

Dilated_img = invertAndDilate(grayed_img)

cons = find_Contours(Dilated_img)

labeled_img, OUTPUT = contours(ex_red, cons)
print(OUTPUT)
cv2.imshow("title", labeled_img)

cv2.waitKey(0)
cv2.destroyWindow()
"""