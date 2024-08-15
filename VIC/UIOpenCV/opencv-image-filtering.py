import cv2
import sys
import numpy

PREVIEW  = 0  # Preview Mode
BLUR     = 1  # Blurring Filter
FEATURES = 2  # Corner Feature Detector
CANNY    = 3  # Canny Edge Detector
NUEVO    = -1

feature_params = dict(maxCorners=500, qualityLevel=0.2, minDistance=15, blockSize=9)

image_filter = PREVIEW
alive = True

win_name = "Presiona las teclas: [B,C,F,N,P,Q]"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

source = cv2.VideoCapture(0)

while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break

    frame = cv2.flip(frame, 1)

    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result = cv2.Canny(frame, 80, 150)
    elif image_filter == BLUR:
        result = cv2.blur(frame, (13, 13))
    elif image_filter == FEATURES:
        result = frame
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
        if corners is not None:
            for corner in corners:
                x, y = corner.ravel()
                cv2.circle(result, (int(x), int(y)), 10, (0, 255, 0), 1)
        result = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif image_filter == NUEVO:
        result = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q") or key == 27:
        alive = False
    elif key == ord("C") or key == ord("c"):
        image_filter = CANNY
    elif key == ord("B") or key == ord("b"):
        image_filter = BLUR
    elif key == ord("F") or key == ord("f"):
        image_filter = FEATURES
    elif key == ord("P") or key == ord("p"):
        image_filter = PREVIEW
    elif key == ord("N") or key == ord("n"):
        image_filter = NUEVO

source.release()
cv2.destroyWindow(win_name)
