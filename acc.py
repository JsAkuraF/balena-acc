from sense_hat import SenseHat

sense = SenseHat()

while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x=round(x, 0)
	y=round(y, 0)
	z=round(z, 0)
	message = 'Temperature is %d F Humidity is %d percent Pressure is %d mbars' %(x,y,z)

	sense.show_message(message, scroll_speed=(0.00),text_colour=[200,0,200], back_colour= [0,0,0])