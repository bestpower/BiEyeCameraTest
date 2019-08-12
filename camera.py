import cv2
import numpy as np
import time
# from mtcnn.detect_face import MTCNN

capture1 = cv2.VideoCapture(0)
time.sleep(1)
capture2 = cv2.VideoCapture(1)

# mtcnn = MTCNN()
while (True):
    ret1, frame1 = capture1.read()
    time.sleep(1)
    ret2, frame2 = capture2.read()

    frame1 = cv2.resize(frame1, (640, 480))
    time.sleep(1)
    frame2 = cv2.resize(frame2, (640, 480))

    # boxes, landmarks_mtcnn = mtcnn.predict(frame1)
    # for box in boxes:
    #     score = box[4]
    #     x1, y1, x2, y2 = (box[:4]+0.5).astype(np.int32)
    #
    #     w = x2 - x1 + 1
    #     h = y2 - y1 + 1
    #     size = int(max([w, h])*1.1)
    #     cx = x1 + w//2
    #     cy = y1 + h//2
    #     x1 = cx - size//2
    #     x2 = x1 + size
    #     y1 = cy - size//2
    #     y2 = y1 + size
    #
    #     print(x1, y1, x2, y2)
    #
    #     cv2.rectangle(frame1, (x1, y1), (x2, y2), (0, 0, 255), 2)
    #     cv2.rectangle(frame2, (x1+50, y1), (x2+50, y2), (0, 0, 255), 2) # between ir camear and rgb camear have 50 distance

    frame = np.hstack((frame1, frame2))
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.05)

capture1.release()
capture2.release()
cv2.destroyAllWindows()


