import serial
import time

arduino_integrated = serial.Serial('/dev/ttyACM0', 9600)

arduino_integrated.timeout=0.5
arduino_integrated.bytesize=8
arduino_integrated.stopbits=1

message_delay = 2		# s
last_time_sent = 0		# s
while True:
	t = time.time()
	if t - last_time_sent > message_delay:
		arduino_integrated.write(f"Leonardo sent - {time.localtime().tm_hour:02d}:{time.localtime().tm_min:02d}:{time.localtime().tm_sec:02d}".encode('utf-8'))
		last_time_sent = t

	message = arduino_integrated.readline()
	if message != b'':
		print('Leonardo received -', message) 

