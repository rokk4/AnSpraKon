#!/usr/bin/env python

from threading import Thread, Lock
import cv2


class WebcamVideoStream:
    def __init__(self, src=0):
        self.thread = Thread(target=self.update, args=())
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.started = False
        self.read_lock = Lock()

    def start(self):
        if self.started:
            print("already started!!")
            return None
        self.started = True
        self.thread.start()
        return self

    def update(self):
        while self.started:
            (grabbed, stream_frame) = self.stream.read()
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, stream_frame
            self.read_lock.release()

    def read(self):
        self.read_lock.acquire()
        cam_frame = self.frame.copy()
        self.read_lock.release()
        return cam_frame

    def stop(self):
        self.started = False
        self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stream.release()

