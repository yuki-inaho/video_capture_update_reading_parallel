import cv2
from camera_class import CameraManager

cam = CameraManager(0)
cam.start()
key = cv2.waitKey(10)
while key & 0xFF != ord('q'):
    if cam.is_grabbed:
        img = cam.frame
        cv2.imshow("test", img)
    key = cv2.waitKey(10)
cam.stop()
cv2.destroyAllWindows()
