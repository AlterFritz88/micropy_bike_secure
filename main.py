import pyb
import utime
acc = pyb.Accel()
led = pyb.LED(1)
sw = pyb.Switch()
status = 'off'

sirena_1 = pyb.LED(2)
sirena_2 = pyb.LED(3)

def press_button():
	global status, led
	if status == 'off':
		status = 'on'
		led.on()
	elif status == 'on':
		status = 'off'
		led.off()


sw.callback(press_button)
while 1:	
	if status == 'on':
		acc_x_1 = acc.x()
		acc_y_1 = acc.y()
		acc_z_1 = acc.z()
		utime.sleep_ms(100)
		acc_x_2 = acc.x()
		acc_y_2 = acc.y()
		acc_z_2 = acc.z()
		if (abs(acc_x_1 - acc_x_2) > 2) or (abs(acc_y_1 - acc_y_2) > 2) or (abs(acc_z_1 - acc_z_2) > 2):
			for i in range(20):
				if status == 'off':
					break
				else:
					sirena_1.on()
					sirena_2.off()			
					utime.sleep_ms(200)
					sirena_1.off()
					sirena_2.on()
					utime.sleep_ms(200)
			sirena_1.off()
			sirena_2.off()
			
		utime.sleep_ms(100)
