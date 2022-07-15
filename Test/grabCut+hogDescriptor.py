import numpy as np
import cv2
import random

cap = cv2.VideoCapture('./source/pedestrian.avi')

hog = cv2.HOGDescriptor((48,96),(16,16),(8,8),(8,8),9)
hog.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()

    if not ret: break

    detected, prop = hog.detectMultiScale(frame)
    
    for (x,y,w,h), p in list(zip(detected, prop)):
        if p < 1.0: continue

        mask = np.zeros((height, width), dtype = np.uint8)
        c = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
         
        cv2.grabCut(frame, mask, (x,y,w,h), None, None, 1, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype(np.uint8)
        processed = frame * mask2[:,:, np.newaxis]

        cv2.rectangle(processed, (x,y,w,h), c, 3)
        cv2.putText(processed, 'prop: {:.2f}'.format(p), (x+w, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, c, 2)
    
    cv2.imshow('processed', processed)
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) == 27: break

cv2.destroyAllWindows()