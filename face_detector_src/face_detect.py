#!/usr/bin/env python3

import numpy as np
import cv2 as cv
import time

import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="sthiruvallur-desktop"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="detect_faces"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    main()

def draw_str(dst, target, s):
    x, y = target
    cv.putText(dst, s, (x+1, y+1), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv.LINE_AA)
    cv.putText(dst, s, (x, y), cv.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv.LINE_AA)

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        print("ERROR: A Face has not been detected")
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

def clock():
    return cv.getTickCount() / cv.getTickFrequency()

def main():
    face_cascade = cv.CascadeClassifier('/media/code/haarcascade_frontalface_default.xml')
    cap = cv.VideoCapture(0)

    while True:
        _ret, img = cap.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.equalizeHist(gray)

        t = clock()
        rects = detect(gray, face_cascade)
        if len(rects) == 0:
            continue   

        vis = gray.copy()
        draw_rects(vis, rects, (0, 255, 0))
        dt = clock() - t

        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000)) 
        cv.imshow('facedetect', vis)
        for x1,y1,x2,y2 in rects:
            face_crop = gray[y1:y2, x1:x2]
            #face_img = cv.imshow('face', face_crop)
            rc,png = cv.imencode('.png', face_crop)
            print("Return code from imencode={}".format(rc))
            msg = png.tobytes()
            local_mqttclient.publish(LOCAL_MQTT_TOPIC,payload=msg,qos=1,retain=False)

        if cv.waitKey(0) & 0xFF == ord('q'):
            break
    
    cap.release()
    print('Done')

if __name__ == '__main__':
    local_mqttclient = mqtt.Client()
    local_mqttclient.on_connect = on_connect_local
    local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

    # go into a loop
    local_mqttclient.loop_forever()
    cv.destroyAllWindows()
