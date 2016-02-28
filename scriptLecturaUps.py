#!/usr/bin/python
 
import serial

aux = 0
 
PuertoSerie = serial.Serial('./ptyp1', 9600, rtscts=True, dsrdtr=True)

while True:
  data = PuertoSerie.readline()
  
  if data[0] == ":":	
  	for x in data[1:7]:
  		checksum = checksum ^ ord(x)
  	
  
