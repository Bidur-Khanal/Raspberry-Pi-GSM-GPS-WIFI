import serial
import RPi.GPIO as GPIO
import os, time
import re
import changewifi

GPIO.setmode(GPIO.BOARD)
port =serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1)  #"/dev/ttyS0" for raspberrypi zero, "/dev/ttyAMA0" for raspberrypi 3





##########function to send message############
def send_message( number, message):

 print number
 print message
 port.write('AT'+'\r\n') # check the GSM+GPRS module, should return OK if working
 receive= port.read(100)
 print receive
 time.sleep(1)
 
 port.write('AT+CMGF=1'+'\r\n')# set to text mode
 receive= port.read(100)
 print receive
 time.sleep(1)
 
 port.write('AT+CSMP= 17,167,0,4'+'\r\n')# for encoding bytes and other parameters
 receive= port.read(100)
 print receive
 time.sleep(1)
 
 AT_number='AT+CMGS="{n}"'.format(n=number)
 
 port.write(AT_number+'\r\n')# the number where message is to be sent
 receive= port.read(100)
 print receive
 time.sleep(1)
 
 port.write(message+'\r\n')# the message text
 receive = port.read(100)
 print receive
 
 port.write('\x1A')
 for i in range(10):
  receive= port.read(1000) # read the response from the service provider if additional information sent
  print receive






###########function to ON and OFF GPS#############

def ONOFF_GPS(ONOFF):

   
 if (ONOFF ==1):    
  port.write('AT+GPS=1'+'\r\n')# open GPS
  receive= port.read(1000)
  print receive
  time.sleep(1)
  port.write('AT+GPSRD=10'+'\r\n')# get NEMA information in every 10 seconds 
  receive=port.read(1000)
  print receive
 else:
  port.write('AT+GPS=0'+'\r\n')# off GPS
  receive= port.read(1000)
  print receive
  time.sleep(1)
  





###########function to set where to store messages############      
def Set_message_storage():
 port.write('AT+CPMS="SM","SM","SM"'+'\r\n')# set the storage memory for messages// here all three set to SIM
 receive= port.read(100)
 print receive
 time.sleep(1)






 
###########function to read stored messages#############
def read_stored_message():
 port.write('AT+CMGF=1'+'\r\n')# set to test mode
 receive= port.read(1000)
 print receive
 time.sleep(1)

 port.write('AT+CMGL="ALL"'+'\r\n')# list the messages
 send=""
 for i in range(5):
  receive= port.read(1000) # read the response from the service provider if additional information sent
  send= send+receive
 return send 
 
 
 '''port.write('AT+CMGR=5'+'\r\n')# read a particular message with the index value
 receive= port.read(1000)
 print receive
 time.sleep(1)'''




###########function to send data using tcp#############
def send_data():

 '''port.write('AT+CIPSHUT'+'\r\n')# SHUTDOWN IF ANY EXISTING CONNECTION
 receive= port.read(1000)
 print receive
 time.sleep(1)'''
 
 port.write('AT+CIPSTART="TCP","192.168.100.12",50'+'\r\n')# OPEN TCP CONNECTION
 receive= port.read(1000)
 print receive
 time.sleep(1)
 port.write('AT+CIPSEND'+'\r\n')# SEND THE DATA
 receive= port.read(1000)
 print receive
 time.sleep(1)
 port.write('DATA TO BE SENT'+'\r\n')# DATA
 receive= port.read(1000)
 print receive
 time.sleep(1)
 port.write('\x1A')
 receive= port.read(1000)
 print receive
 time.sleep(1)
 port.write('AT+CIPCLOSE'+'\r\n')# CLOSE TCP CONNECTION
 receive= port.read(1000)
 print receive
 time.sleep(1)
 port.write('AT+CIPSHUT'+'\r\n')# DISCONNECTS THE WIRELESS CONNECTION
 receive= port.read(1000)
 print receive
 time.sleep(1)
 



    

'''***********************************************
port.write('AT+CSDH=1'+'\r\n')# show the value in result code
receive= port.read(100)
print receive
time.sleep(1)
port.write('AT+CNMI?'+'\r\n')#new message indications
receive= port.read(100)
print receive
time.sleep(1)
**************************************************'''



############## function just to read the port##############
def read_me():
  time.sleep(1)
  receive= port.read(1000) # read the response from the service provider
  return receive

  

def format_match(value):
    r= re. compile('ssid=.*,psk=.*')
    #s= 'Ssid=Office,psk=12345'.lower()
    if r.match(value):
        print 'format matches'
        return 1
        
    else:
        print 'check the format!!'
        return 0



if __name__ == '__main__':

    #send_message( "+9779849811***", "Hello")
    #send_data()
    ONOFF_AGPS(1)
	
    '''while 1:
     read_string= read_me()
     print read_string'''
     

    #######continuosly read sms in a poll for wifi SSID and Password##########
    while 1:
     read= read_me()   
     #read=read_stored_message()
     print read
     read1= read.split('\n')
     for i in range(len(read1)):
      if read1[i].lower().startswith('ssid'):
         if format_match(read1[i].lower()): 
          read2=read1[i].split(',')
          print read2
          read_ssid=  read2[0].split('=')
          read_psk= read2[1].split('=')
          ssid= read_ssid[1]
          psk= read_psk[1]
          psk=psk[:-1]
          changewifi.connect(ssid,psk)
                
               
    
        
    #print read_stored_message()
    
    
    
