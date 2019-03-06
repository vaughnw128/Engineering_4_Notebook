#Vaughn and Charlie's I2C setup
import time
import RPi.GPIO as GPIO

#Setup LSM303
import Adafruit_LSM303
lsm303 = Adafruit_LSM303.LSM303()

#Setup SSD1306
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

while(True):
	#Clear the display
	#Print header
	draw.text((0, 0), 'ACCELEROMETER DATA',  font=font, fill=255)
	# Read the X, Y, Z axis acceleration values and print them.
	accel, mag = lsm303.read()
	# Grab the X, Y, Z components from the reading and print them out.
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag
	xFloat = float(accel_x)/100
	#Prints X, Y, Z, to display
	draw.text((0, 20),('X: {}'.format(accel_x/100)), font=font, fill=255)
	draw.text((0, 30),('Y: {}'.format(accel_y/100)), font=font, fill=255)
	draw.text((0, 40),('Z: {}'.format(accel_z/100)), font=font, fill=255)
	# Wait half a second and repeat.
	time.sleep(0.5)
	#Display
	disp.image(image)
	disp.display()
	disp.clear()
	draw.rectangle((0,0,width,height), outline=0, fill=0)

