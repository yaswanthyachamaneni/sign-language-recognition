import cv2
import numpy as np
vc = cv2.VideoCapture(0)
pic_no = 0
total_pic = 1200
flag_capturing = False
path = 'D:/Sign_language_recognition/Dataset/Training/Good/'
while(True):
    # read image
    rval, frame = vc.read()
    frame = cv2.flip(frame, 1)
    
    # get hand data from the rectangle sub window on the screen
    cv2.rectangle(frame, (300,300), (100,100), (255,0,0),2)
    
    cv2.imshow("image", frame)
    crop_img = frame[100:300, 100:300]
    if flag_capturing:
        
        pic_no += 1
        save_img = cv2.resize( crop_img, (50,50) )
        save_img = np.array(save_img)
        cv2.imwrite(path + "/" + str(pic_no) + ".jpg", save_img)
        
    keypress = cv2.waitKey(1)
    
    if pic_no == total_pic:
        flag_capturing = False
        break
    
    if keypress == ord('q'):
        break
    elif keypress == ord('c'):
        flag_capturing = True

print(pic_no)
vc.release()
cv2.destroyAllWindows()