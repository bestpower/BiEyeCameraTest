# if __name__ == '__main__':
#     import sys, platform
#     from PyQt5.QtWidgets import QApplication
#     from CvPyGui import Main
#
#     if platform.system() == "Windows":
#         import ctypes
#
#         ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
#
#     app = QApplication(sys.argv)
#     window = Main.MyApp()
#     window.show()
#     global update1
#     update1 = 0
#     global update2
#     update2 = 0
#     sys.exit(app.exec_())


import cv2
import numpy as np


cap1 = cv2.VideoCapture(1)
cv2.VideoCapture.set(cap1, 3, 270)  # 这里Property identifier要求是int
cv2.VideoCapture.set(cap1, 4, 270)  # 见下图,3表示CV_CAP_PROP_FRAME_WIDTH,设为270.（设为1和270的效果一样）

cap2 = cv2.VideoCapture(0)
cv2.VideoCapture.set(cap2, 3, 1)
cv2.VideoCapture.set(cap2, 4, 1)
# ret = cap.set(3, 320)
# ret = cap.set(4, 240)
# 设置摄像头分辨率
# cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


i = 0
while cap1.isOpened() and cap2.isOpened():
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    # cv2.resize(frame1, (640, 480))
    # cv2.resize(frame2, (640, 480))
    left_img = frame1
    right_img = frame2
    if ret1 and ret2:
        # 显示两幅图片合成的图片
        # cv2.imshow('img', frame)
        # 显示左摄像头视图
        cv2.imshow('left', left_img)
        # 显示右摄像头视图
        cv2.imshow('right', right_img)
    key = cv2.waitKey(delay=2)
    if key == ord('t'):
        cv2.imwrite('./img/test1' + str(i) + '.jpg', frame1)  #
        cv2.imwrite('./img/test2' + str(i) + '.jpg', frame2)  #
        i += 1
    if key == ord("q") or key == 27:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()


# cap1 = cv2.VideoCapture(1)
# cap2 = cv2.VideoCapture(0)
#  + cv2.CAP_DSHOW

# while True:
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()
#     cv2.imshow('frame1', frame1)
#     cv2.imshow('frame2', frame2)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap1.release()
# cap2.release()
# cv2.destroyAllWindows()
