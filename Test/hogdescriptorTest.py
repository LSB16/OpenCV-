import cv2
import random

cap = cv2.VideoCapture('./source/pedestrian.avi')

#hog = cv2.HOGDescriptor()
#hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

hog = cv2.HOGDescriptor((48,96),(16,16),(8,8),(8,8),9)
hog.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())

while True:
    ret, frame = cap.read()

    if not ret: break

    detected, prop = hog.detectMultiScale(frame)
    
    for (x,y,w,h), p in list(zip(detected, prop)):
        if p < 1.0: continue
        c = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
        cv2.rectangle(frame, (x,y,w,h), c, 3)
        cv2.putText(frame, 'prop: {:.2f}'.format(p), (x+w, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, c, 2)
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) == 27: break

cv2.destroyAllWindows()