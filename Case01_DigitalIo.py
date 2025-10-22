import RPi.GPIO as GIPIO #llamar la libreria que permite utilizar los pines GPIO, y renombraria de una manera simple
import time #llamar a la libreria que permite trabajar con funciones de manejo de tiempo 

PIN_BOTON = 3
PIN_LED = 7

estadoBoton = 0 #inicializar una variable para almacenar el estado de el boton

GPIO.setmode(GPIO.BOARD) #confiurar los pines de la raspberry segun la numeracion fisica 
GPIO.setup(7,GPIO.OUT) #configurar el pin fisico 7 como salida
GPIO.setup(3,GPIO.IN) #configurar pin fisico 3 como entrada

while True: #ciclo infinito (void loop)
	estadoBoton = GPIO.input(PIN_BOTON) #leer entrada digital
	GPIO.output(7, estadoBoton) #enviar el estado del boton al pin 7 (digitalWrite)
	if estadoBoton == 1 #si el boton esta precionado entonces:
		print("ENCENDIDO") #imprime mensaje encendido
		time.sleep(1) #realizar una pausa de un seg
	else: #si no esta encendido imprima:
		print("apagado") #esta apagado
		tiem.sleep(1)
