#!/usr/bin/python
 
import serial
import time

def statusBateria(status):
	if status == "00":
		return "normal"
	if status == "01":
		return "bateria"
	if status == "02":
		return "shutdown"

def grabartxt(status, bateria, carga):
    archivoDatos=open('datos.txt','a')
    archivoDatos.write(time.strftime("%c") + '\n')
    archivoDatos.write("Estatus: " + status + '\n')
    archivoDatos.write("Bateria: " + bateria + '\n')
    archivoDatos.write("Carga: " + carga + '\n')
    archivoDatos.close()

checksum = 0
 
PuertoSerie = serial.Serial('./ptyp1', 9600, rtscts=True, dsrdtr=True)

while True:
  data = PuertoSerie.readline()
  
  if data[0] == ":":	
  	for x in data[1:7]:
  		checksum = checksum ^ ord(x)

  if hex(checksum) == "0x" + data[7:9]:
    status = statusBateria(data[1:3])

    bateriaAux = str(int(data[3:5],16))
    bateria = bateriaAux[0:2] + "." + bateriaAux[2]

    cargaAux = str(int(data[5:7],16))
    carga = cargaAux[0:2] + "." + cargaAux[2]

    grabartxt(status,bateria,carga)

  if status == "shutdown":
    print "apagando... \n"

  checksum = 0