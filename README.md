##### This repo contains codes to perform following operations in raspberry PI zero/3 Model B interfacing with A7 AI Thinker GSM/GPRS module :

1. Sent a message using A7 AI Thinker GSM/GPRS module.

2. Get the GPS NMEA information.

3. receive SMS with ssid and password in a format, read the sms and automatically connect to the given wifi in the raspberry pi Zero.

4. Send the DATA to a network over TCP using A7 AI Thinker GSM/GPRS module.

***

![alt text](https://i.stack.imgur.com/yHddo.png "Raspberry Pi Zero")
![alt text](http://www.icstation.com/images/big/products/11470_4_2239.JPG "A7 AI Thinker")

+ First, Connect **A7 AI Thinker UART** to **Raspberry Pi Zero UART** *(Tx/Rx = Rx/Tx)*.
+ Run, ```gsm2.py```. The program polls for the matching SMS. If a match is found, connects the **Raspberry Pi Zero** to that WIFI.

* Note: Change string format in ```gsm2.py``` to modify sms format.

