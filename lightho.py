import time
import coloredlogs
from tuyalinksdk.client import TuyaClient
from tuyalinksdk.console_qrcode import qrcode_generate
coloredlogs.install(level='DEBUG')
import sys
import serial
import time

ser = serial.Serial('COM3', 115200)	#Enter your COM Port, which you can get from Arduino IDE..

client = TuyaClient(productid=' ', #Past your Product ID here...
                    uuid='',  #Past your UUID here... 
                    authkey=' ') #Past your KEY here...

def on_connected():
    print('Connected.')

def on_qrcode(url):
    qrcode_generate(url)

def on_reset(data):
    print('Reset:', data)

def on_dps(dps):
    print('DataPoints:', dps)
    if(dps == {'101':True}):
    	print("Christmas Light On.....")
    	time.sleep(0.1)
    	ser.write(b'H')
    	print('ON')
    elif(dps=={'101':False}):
    	print("Christmas Light OFF.....")
    	time.sleep(0.1)
    	ser.write(b'L')
    	print('OFF')
    client.push_dps(dps)

client.on_connected = on_connected
client.on_qrcode = on_qrcode
client.on_reset = on_reset
client.on_dps = on_dps

client.connect()
client.loop_start()

while True:
    time.sleep(1)
