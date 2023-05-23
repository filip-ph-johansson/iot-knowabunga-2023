import os
from typing import Callable

import pyttsx3
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected to the mqtt server")
    
    client.subscribe("/ttv/unknown")
    client.subscribe("/ttv/inbound")
    client.subscribe("/ttv/outbound")

def bind_on_message(textToSpeech: Callable[[str], None]):
	def on_message(client, userdata, msg):
		# The callback for when a PUBLISH message is received from the server.
		username = msg.payload.decode("utf-8")

		if msg.topic == "/ttv/unknown":	
			# in this case the username is "unknown" because the tag hasn't been registered in the Kontan app yet.
			textToSpeech("unknown user detected")
		elif msg.topic == "/ttv/inbound":
			textToSpeech(f"welcome {username}")
		elif msg.topic == "/ttv/outbound":
			textToSpeech(f"goodbye {username}")

	return on_message

def main():
	mqtt_hostname = os.environ.get("MQTT_HOSTNAME", "10.11.15.95")
	mqtt_port = int(os.environ.get("MQTT_PORT", "1883"))

	engine = pyttsx3.init()
	engine.setProperty('rate', 50) # this property controls the voice speed

	def textToSpeech(text: str):
		engine.say(text)
		engine.runAndWait()
		
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = bind_on_message(textToSpeech)
	client.connect(mqtt_hostname, mqtt_port, 60)

	# Blocking call that processes network traffic, dispatches callbacks and
	# handles reconnecting.
	# Other loop*() functions are available that give a threaded interface and a
	# manual interface.
	client.loop_forever()

if __name__ == "__main__":
	main()