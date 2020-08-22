import cv2
import parinya
cap = cv2.VideoCapture(0)
yolo = parinya.YOLOv3('coco.names','yolov3-tiny.cfg','yolov3-tiny.weights')
while True:
    _, frame = cap.read()
    yolo.detect(frame)
    cv2.imshow('frame',frame)
    cv2.waitKey(1)