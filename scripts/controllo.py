#!/usr/bin/python

import sys
import socket
import RPi.GPIO as GPIO

def accensione_ventola():
    print "Accendo ventola"
    GPIO.output(ventola,True)    

def spegnimento_ventola():
    print "Spengo ventola"
    GPIO.output(ventola,False)    

def stampa_stato():
    print "Stampo stato"


port = 5001
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("",port))
server_socket.listen(5)

ventola=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(ventola,GPIO.OUT)

print "Pronto sulla porta ", port

try: 
   while True:
       client_socket, address =server_socket.accept()
       print "Connection from ", address
       data = client_socket.recv(512)
       print "RECIEVED:" , data
       if data == 'accendi':
          accensione_ventola()
       if data == 'spegni':
          spegnimento_ventola()
       if data == 'status':
          stampa_stato()

except KeyboardInterrupt:
     print "Program interrupted"
  
except:
     print "Program aborted with unexpected error: ", sys.exc_info()[0]

finally:
   print "Cleaning up GPIO..."
   ret=GPIO.cleanup()
   print "GPIO cleaned up ",ret
   print "Closing socket..."   	
   ret=server_socket.close()
   print "socket closed ",ret 

