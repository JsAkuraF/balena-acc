from sense_hat import SenseHat
import time
sense = SenseHat()

while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x=round(x, 0)
	y=round(y, 0)
	z=round(z, 0)
	message = '%d, %d, %d' %(x,y,z)

	sense.show_message(message, scroll_speed=(0.05),text_colour=[200,0,200], back_colour= [0,0,0])
	time.sleep(1)