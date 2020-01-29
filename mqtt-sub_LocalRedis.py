#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import redis

#broker_address = "127.0.0.1"
broker_address = "test.mosquitto.org"
#broker_address = "172.20.10.2"
#RedisHost = "127.0.0.1"
RedisHost = "redis-14787.c82.us-east-1-2.ec2.cloud.redislabs.com"
#Topic = "Miho-MQTT"
Topic = "Imamura_test"

#r = redis.Redis(host=RedisHost, port='6379')
r = redis.Redis(host=RedisHost, port='14787', password='50T5RWVcwdpQrFXkq26rTxgQwc7Ru1c7')

def on_message(client, userdata, message):
    m = str(message.payload.decode("utf-8"))
    print("message received " + m)
#    r.set('RPIvalue',m)
    r.set('Imamura_RPIvalue',m)
#    print("message topic=",message.topic)
#    print("message qos=",message.qos)
#    print("message retain flag=",message.retain)


print("creating new instance")
client = mqtt.Client() #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop

while True:
    client.subscribe(Topic)
    time.sleep(2) # wait

client.loop_stop() #stop the loop

