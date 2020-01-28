#!/usr/bin/env python3

import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST="sthiruvallur-desktop"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="detect_faces"

CLOUD_MQTT_HOST="169.62.47.162"
CLOUD_MQTT_PORT=1883
CLOUD_MQTT_TOPIC="persist_faces"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))

def on_connect_cloud(client, userdata, flags, rc):
    print("connect to cloud broker with rc: " + str(rc))
	
def on_message(client,userdata, msg):
  try:
    print("message received!")
    print("Received message: len:{} bytes from topic:{}".format(len(msg.payload), msg.topic) )
    # Publishing this message to the cloud broker
    msg = msg.payload
    cloud_mqttclient.publish(CLOUD_MQTT_TOPIC, payload=msg, qos=1, retain=True)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

local_mqttclient.subscribe(LOCAL_MQTT_TOPIC, qos=2)
local_mqttclient.on_message = on_message

cloud_mqttclient = mqtt.Client()
cloud_mqttclient.on_connect = on_connect_cloud
cloud_mqttclient.connect(CLOUD_MQTT_HOST, CLOUD_MQTT_PORT, 60)



# go into a loop
local_mqttclient.loop_forever()
#cloud_mqttclient.loop_forever()


