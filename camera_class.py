import cv2
import numpy as np
from threading import Thread


class CameraManager:
    def __init__(self, device_id=0):
        self._is_grabbed = False
        self._frame = np.array([])
        self.stream = cv2.VideoCapture(device_id)
        self.stopped = False

    def start(self):
        self.thread_ = Thread(target=self.update, args=())
        self.thread_.daemon = True  # daemonize this thread
        self.thread_.start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            (self._is_grabbed, self._frame) = self.stream.read()

    def stop(self):
        self.stopped = True

    @property
    def frame(self):
        return self._frame

    @property
    def is_grabbed(self):
        return self._is_grabbed
