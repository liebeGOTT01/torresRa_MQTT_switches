from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        cp.red_led = True
        client.subscribe("cpx-switch/#")

def on_message(client, userdata, msg):
 
    if msg.payload.decode() == "true" and msg.topic == "cpx-switch/0":   #to check if it is on and to is clicking at the switch for index[0]
        cp.pixels[0] = (255, 255, 255)                                              #light color
    elif msg.payload.decode() == "false" and msg.topic == "cpx-switch/0":      #to turn off the switch with light set to color none
        cp.pixels[0] = (0, 0, 0)

    elif msg.payload.decode() == "true" and msg.topic == "cpx-switch/1":    #to check if it is on and to is clicking at the switch for index[1]
        cp.pixels[1] = (255, 255, 255)
    elif msg.payload.decode() == "false" and msg.topic == "cpx-switch/1":        #to turn off the switch with light set to color none
        cp.pixels[1] = (0, 0, 0)

    elif msg.payload.decode() == "true" and msg.topic == "cpx-switch/2":     #to check if it is on and to is clicking at the switch for index[2]
        cp.pixels[2] = (255, 255, 255)
    elif msg.payload.decode() == "false" and msg.topic == "cpx-switch/2":        #to turn off the switch with light set to color none
        cp.pixels[2] = (0, 0, 0)

cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqttrounded