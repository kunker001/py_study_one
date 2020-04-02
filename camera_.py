import cv2
import os
import threading
import time
import email_



print("=============================================")
print("=  会自动拍4张照片！                         =")
print("=============================================")
print()

flag = True
index = 1
cap = cv2.VideoCapture(0)
width = 640
height = 480
w = 360
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

crop_w_start = (width-w)//2
crop_h_start = (height-w)//2

print(width, height)
img_path = "image"
if os.path.exists(img_path) is False:
    os.mkdir(img_path)

#拍照方法     
# def camera_func():
#     global index
#     while flag:
#         time.sleep(5)
#         cv2.imwrite("%s/%d.jpeg" % (img_path, index),
#                     cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA))
#         print("%s: %d 张图片" % (img_path, index))
#         index += 1

#拍照线程启动
# timer = threading.Timer(5, camera_func)
# timer.start()
while True:
    # get a frame
    ret, frame = cap.read()
    # show a frame
    frame = frame[crop_h_start:crop_h_start+w, crop_w_start:crop_w_start+w]
    frame = cv2.flip(frame,1,dst=None)
    #cv2.imshow("capture", frame)
    cv2.imwrite("%s/%d.jpeg" % (img_path, index),frame)
    print("%s: %d 张图片" % (img_path, index))
    index += 1
    if(index >= 5):
        print("end")
        break
    time.sleep(5)
    # input = cv2.waitKey(1) & 0xFF
    # class_name = img_path 
    # if input == ord('q'):
    #     flag = False
    #     break
cap.release()
cv2.destroyAllWindows()
