#!/usr/bin/env python3

import numpy as np
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="127.0.0.1"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="detect_faces"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

#status = True
i = 0;
while True:
    print("I am printing {}".format(i))
    i = i + 1
    if i == 10:
        break

# go into a loop
local_mqttclient.loop_forever()



