import cv2
import numpy as np

def one():
    img = cv2.imread("1.png")
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    result_red = cv2.bitwise_and(img, img, mask=mask_red)
    result_blue = cv2.bitwise_and(img, img, mask=mask_blue)



    lower_green = np.array([35, 50, 50])  
    upper_green = np.array([85, 255, 255])


    lower_brown = np.array([10, 50, 50])   
    upper_brown = np.array([20, 255, 255])

    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)


    modified_img1=img.copy()
    new_color_bgr=(255,234,23)
    modified_img1[np.where(mask_green == 255)] = new_color_bgr

    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)

    new_color_bgr1=(124,252,255)
    modified_img1[np.where(mask_brown == 255)] = new_color_bgr1
    cv2.imshow('modified image 1',modified_img1)
    roi_x=0
    roi_y=420
    roi_width=638
    roi_height=220
    roi1 = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    gray_roi = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)
    blurred_roi = cv2.GaussianBlur(gray_roi, (9, 9), 2)
    edges = cv2.Canny(blurred_roi, threshold1=400, threshold2=500)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_triangles1 = 0

    for contour in contours:
        epsilon = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
    
    
        if len(approx)==3:
            num_triangles1 += 1
            cv2.drawContours(roi, [approx], 0, (0, 255, 0), 1)

    print("Number of triangles in 1:", num_triangles1)


    cv2.imshow("Detected Triangles", roi1)
 




def two():
    img = cv2.imread("2.png")
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    result_red = cv2.bitwise_and(img, img, mask=mask_red)
    result_blue = cv2.bitwise_and(img, img, mask=mask_blue)



    lower_green = np.array([35, 50, 50])  
    upper_green = np.array([85, 255, 255])


    lower_brown = np.array([10, 50, 50])   
    upper_brown = np.array([20, 255, 255])

    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)


    modified_img2=img.copy()
    new_color_bgr=(255,234,23)
    modified_img2[np.where(mask_green == 255)] = new_color_bgr

    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)

    new_color_bgr1=(124,252,255)
    modified_img2[np.where(mask_brown == 255)] = new_color_bgr1
    cv2.imshow('modified image 2',modified_img2)
    roi_x2=344
    roi_y2=0
    roi_width2=290
    roi_height2=369
    roi2 = img[roi_y2:roi_y2+roi_height2, roi_x2:roi_x2+roi_width2]
    gray_roi = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
    blurred_roi = cv2.GaussianBlur(gray_roi, (9, 9), 2)
    edges = cv2.Canny(blurred_roi, threshold1=400, threshold2=500)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_triangles2 = 0
    
    for contour in contours:
        epsilon = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
    
    
        if len(approx)==3:
            num_triangles2 += 1
            cv2.drawContours(roi2, [approx], 0, (0, 255, 0), 1)

    print("Number of triangles in 2:", num_triangles2)


    cv2.imshow("Detected Triangles 2", roi2)


  

def three():
    img = cv2.imread("3.png")
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    result_red = cv2.bitwise_and(img, img, mask=mask_red)
    result_blue = cv2.bitwise_and(img, img, mask=mask_blue)



    lower_green = np.array([35, 50, 50])  
    upper_green = np.array([85, 255, 255])


    lower_brown = np.array([10, 50, 50])   
    upper_brown = np.array([20, 255, 255])

    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)


    modified_img=img.copy()
    new_color_bgr=(255,234,23)
    modified_img[np.where(mask_green == 255)] = new_color_bgr

    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)

    new_color_bgr=(124,252,255)
    modified_img[np.where(mask_brown == 255)] = new_color_bgr
    cv2.imshow('modified image 3',modified_img)
    roi_x=0
    roi_y=0
    roi_width=248
    roi_height=637
    roi = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred_roi = cv2.GaussianBlur(gray_roi, (9, 9), 2)
    edges = cv2.Canny(blurred_roi, threshold1=400, threshold2=500)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_triangles = 0
    
    for contour in contours:
        epsilon = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)


        if len(approx)==3:
            num_triangles += 1
            cv2.drawContours(roi, [approx], 0, (0, 255, 0), 1)

    print("Number of triangles in 3:", num_triangles)


    cv2.imshow("Detected Triangles 3", roi)



def four():
    img = cv2.imread("4.png")
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    result_red = cv2.bitwise_and(img, img, mask=mask_red)
    result_blue = cv2.bitwise_and(img, img, mask=mask_blue)



    lower_green = np.array([35, 50, 50])  
    upper_green = np.array([85, 255, 255])


    lower_brown = np.array([10, 50, 50])   
    upper_brown = np.array([20, 255, 255])

    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)


    modified_img=img.copy()
    new_color_bgr=(255,234,23)
    modified_img[np.where(mask_green == 255)] = new_color_bgr

    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)

    new_color_bgr=(124,252,255)
    modified_img[np.where(mask_brown == 255)] = new_color_bgr
    cv2.imshow('modified image 4',modified_img)
    roi_x=0
    roi_y=0
    roi_width=470
    roi_height=635
    roi = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred_roi = cv2.GaussianBlur(gray_roi, (9, 9), 2)
    edges = cv2.Canny(blurred_roi, threshold1=400, threshold2=500)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_triangles = 0
    
    for contour in contours:
        epsilon = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
    
    
        if len(approx)==3:
            num_triangles += 1
            cv2.drawContours(roi, [approx], 0, (0, 255, 0), 1)

    print("Number of triangles in 4:", num_triangles)


    cv2.imshow("Detected Triangles 4", roi)



def five():
    img = cv2.imread("5.png")
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    result_red = cv2.bitwise_and(img, img, mask=mask_red)
    result_blue = cv2.bitwise_and(img, img, mask=mask_blue)



    lower_green = np.array([35, 50, 50])  
    upper_green = np.array([85, 255, 255])


    lower_brown = np.array([10, 50, 50])   
    upper_brown = np.array([20, 255, 255])

    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)


    modified_img=img.copy()
    new_color_bgr=(255,234,23)
    modified_img[np.where(mask_green == 255)] = new_color_bgr

    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)

    new_color_bgr=(124,252,255)
    modified_img[np.where(mask_brown == 255)] = new_color_bgr
    cv2.imshow('modified image 5',modified_img)
    roi_x=0
    roi_y=480
    roi_width=638
    roi_height=155
    roi = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred_roi = cv2.GaussianBlur(gray_roi, (9, 9), 2)
    edges = cv2.Canny(blurred_roi, threshold1=400, threshold2=500)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_triangles = 0
    
    for contour in contours:
        epsilon = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
    
    
        if len(approx)==3:
            num_triangles += 1
            cv2.drawContours(roi, [approx], 0, (0, 255, 0), 1)

    print("Number of triangles in 5:", num_triangles)


    cv2.imshow("Detected Triangles 5", roi)




def six():
    img = cv2.imread("6.png")
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    result_red = cv2.bitwise_and(img, img, mask=mask_red)
    result_blue = cv2.bitwise_and(img, img, mask=mask_blue)



    lower_green = np.array([35, 50, 50])  
    upper_green = np.array([85, 255, 255])


    lower_brown = np.array([10, 50, 50])   
    upper_brown = np.array([20, 255, 255])

    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)


    modified_img=img.copy()
    new_color_bgr=(255,234,23)
    modified_img[np.where(mask_green == 255)] = new_color_bgr

    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)

    new_color_bgr=(124,252,255)
    modified_img[np.where(mask_brown == 255)] = new_color_bgr
    cv2.imshow('modified image 6',modified_img)
    roi_x=0
    roi_y=0
    roi_width=200
    roi_height=638
    roi = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred_roi = cv2.GaussianBlur(gray_roi, (9, 9), 2)
    edges = cv2.Canny(blurred_roi, threshold1=400, threshold2=500)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_triangles = 0
    
    for contour in contours:
        epsilon = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
    
    
        if len(approx)==3:
            num_triangles += 1
            cv2.drawContours(roi, [approx], 0, (0, 255, 0), 1)

    print("Number of triangles in 6:", num_triangles)


    cv2.imshow("Detected Triangles 6", roi)


    

def seven():
    img = cv2.imread("7.png")
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    result_red = cv2.bitwise_and(img, img, mask=mask_red)
    result_blue = cv2.bitwise_and(img, img, mask=mask_blue)



    lower_green = np.array([35, 50, 50])  
    upper_green = np.array([85, 255, 255])


    lower_brown = np.array([10, 50, 50])   
    upper_brown = np.array([20, 255, 255])

    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)


    modified_img=img.copy()
    new_color_bgr=(255,234,23)
    modified_img[np.where(mask_green == 255)] = new_color_bgr

    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)

    new_color_bgr=(124,252,255)
    modified_img[np.where(mask_brown == 255)] = new_color_bgr
    cv2.imshow('modified image 7',modified_img)
    roi_x=145
    roi_y=0
    roi_width=485
    roi_height=635
    roi = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred_roi = cv2.GaussianBlur(gray_roi, (9, 9), 2)
    edges = cv2.Canny(blurred_roi, threshold1=400, threshold2=500)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_triangles = 0
    
    for contour in contours:
        epsilon = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
    
    
        if len(approx)==3:
            num_triangles += 1
            cv2.drawContours(roi, [approx], 0, (0, 255, 0), 1)

    print("Number of triangles in 7:", num_triangles)


    cv2.imshow("Detected Triangles 7", roi)



def eight():
    img = cv2.imread("8.png")
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    result_red = cv2.bitwise_and(img, img, mask=mask_red)
    result_blue = cv2.bitwise_and(img, img, mask=mask_blue)



    lower_green = np.array([35, 50, 50])  
    upper_green = np.array([85, 255, 255])


    lower_brown = np.array([10, 50, 50])   
    upper_brown = np.array([20, 255, 255])

    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)


    modified_img=img.copy()
    new_color_bgr=(255,234,23)
    modified_img[np.where(mask_green == 255)] = new_color_bgr

    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)

    new_color_bgr=(124,252,255)
    modified_img[np.where(mask_brown == 255)] = new_color_bgr
    cv2.imshow('modified image 8',modified_img)
    roi_x=360
    roi_y=0
    roi_width=270
    roi_height=420
    roi = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred_roi = cv2.GaussianBlur(gray_roi, (9, 9), 2)
    edges = cv2.Canny(blurred_roi, threshold1=400, threshold2=500)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_triangles = 0
    
    for contour in contours:
        epsilon = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
    
    
        if len(approx)==3:
            num_triangles += 1
            cv2.drawContours(roi, [approx], 0, (0, 255, 0), 1)

    print("Number of triangles in 8:", num_triangles)


    cv2.imshow("Detected Triangles 8", roi)



def nine():
    img = cv2.imread("9.png")
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    result_red = cv2.bitwise_and(img, img, mask=mask_red)
    result_blue = cv2.bitwise_and(img, img, mask=mask_blue)



    lower_green = np.array([35, 50, 50])  
    upper_green = np.array([85, 255, 255])


    lower_brown = np.array([10, 50, 50])   
    upper_brown = np.array([20, 255, 255])

    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)


    modified_img=img.copy()
    new_color_bgr=(255,234,23)
    modified_img[np.where(mask_green == 255)] = new_color_bgr

    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)

    new_color_bgr=(124,252,255)
    modified_img[np.where(mask_brown == 255)] = new_color_bgr
    cv2.imshow('modified image 9',modified_img)
    roi_x=0
    roi_y=420
    roi_width=635
    roi_height=210
    roi = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred_roi = cv2.GaussianBlur(gray_roi, (9, 9), 2)
    edges = cv2.Canny(blurred_roi, threshold1=400, threshold2=500)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_triangles = 0
    
    for contour in contours:
        epsilon = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
    
    
        if len(approx)==3:
            num_triangles += 1
            cv2.drawContours(roi, [approx], 0, (0, 255, 0), 1)

    print("Number of triangles in 9:", num_triangles)


    cv2.imshow("Detected Triangles 9", roi)


   

def ten():
    img = cv2.imread("10.png")
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    result_red = cv2.bitwise_and(img, img, mask=mask_red)
    result_blue = cv2.bitwise_and(img, img, mask=mask_blue)



    lower_green = np.array([35, 50, 50])  
    upper_green = np.array([85, 255, 255])


    lower_brown = np.array([10, 50, 50])   
    upper_brown = np.array([20, 255, 255])

    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)


    modified_img=img.copy()
    new_color_bgr=(255,234,23)
    modified_img[np.where(mask_green == 255)] = new_color_bgr

    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)

    new_color_bgr=(124,252,255)
    modified_img[np.where(mask_brown == 255)] = new_color_bgr
    cv2.imshow('modified image 10',modified_img)
    roi_x=0
    roi_y=0
    roi_width=220
    roi_height=635
    roi = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred_roi = cv2.GaussianBlur(gray_roi, (9, 9), 2)
    edges = cv2.Canny(blurred_roi, threshold1=400, threshold2=500)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_triangles = 0
    
    for contour in contours:
        epsilon = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
    
    
        if len(approx)==3:
            num_triangles += 1
            cv2.drawContours(roi, [approx], 0, (0, 255, 0), 1)

    print("Number of triangles in 10:", num_triangles)


    cv2.imshow("Detected Triangles 10", roi)


  
   

def menu():
    print("""1 to access 1st image
2 to access 2nd image
3 to access 3rd image
4 to access 4th image
5 to access 5th image
6 to access 6th image
7 to access 7th image
8 to access 8th image
9 to access 9th image
10 to access 10th image""") 
    n=int(input('enter the image you want to inspect: '))
    while True:
        if n==1:
            one()
        if n==2:
            two()
        if n==3:
            three()
        if n==4:
            four()
        if n==5:
            five()
        if n==6:
            six()
        if n==7:
            seven()
        if n==8:
            eight()
        if n==9:
            nine()
        if n==10:
            ten()
        else:
            break
menu()
cv2.waitKey(0)
cv2.destroyAllWindows()





