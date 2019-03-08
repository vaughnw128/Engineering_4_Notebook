
#Vaughn and Charlie's I2C setup
#MAR 7 2019 /// C0MPLETE
import time
import RPi.GPIO as GPIO
from numpy import interp

#Setup LSM303
import Adafruit_LSM303
lsm303 = Adafruit_LSM303.LSM303()

#Setup SSD1306
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#Define everything for SSD1306
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

#Defining things for moving average
size = 15
movingAverageX = [0.00] * size
movingAverageY = [0.00] * size

#Defining coordinate points
center = [width/2, height/2]
ballPos = [0.00] * 2
#Takes a moving average of all X and Y accelerometer values at a specified size
def movingAverage(accel, movingAverage):
	#Handles the list with arrayHandler
	listHandler(movingAverage, accel, size)

	#Taking a sum of all values in movingAverageX or Y
	sum = 0.00

	#Adds them
	for i in range(0, size):
		sum += movingAverage[i]

	return sum/size

#Adds and removes elements from the list
def listHandler(list, add, size):
	for i in range(0, size-1):
		list[i] = list[i+1]
	list[size-1] = add

#TODO: IMPLEMENT LOCATION FINDER, USE MAG OF LOCATION VECTOR TO DETERMINE ROLL SPEED, DONT LET ROLL OFF SCREEN

#Gets position based on which quadrant it's in
def getPos(dist):


#Gets which quadrant a position is in
def getQuadrant(dist):
	if dist[0] >= width/2:
		if dist[1] >= height/2:
			return 4
		else:
			return 1
	else:
		if dist[1] >= height/2:
			return 2
		else:
			return 3

#Loops the code
while(True):
	# Read the X, Y, Z axis acceleration values and print them.
	accel, mag = lsm303.read()

	# Grab the X, Y, Z components from the reading and print them out.
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag

	#Maps the inputs useing numpy.interp to get it to the right size of the screen
	dist[0] = interp(accel_x,[-1000,1000],[1,0])*disp.width*2
	dist[1] = interp(accel_y,[-1000,1000],[0,1])*disp.height*2

	#Takes moving average of the values
	avLocX = movingAverage(dist[0], movingAverageX)
	avLocY = movingAverage(distY[1], movingAverageY)

	#Uses a bounding box to create a circle based on the values specified by the accelerometers
	eX, eY = 10, 10
	bbox = (avLocX/2 - eX/2, avLocY/2 - eY/2, avLocX/2 + eX/2, avLocY/2 + eY/2)

	#Draws the ellipse
	draw.ellipse(bbox, fill=128)

	#Prints values
	draw.text((0, 50),('{}'.format(round(width, 2))), font=font, fill=255)
	draw.text((35, 50),('{}'.format(round(height, 2))), font=font, fill=255)

	#Display and then clear
	disp.image(image)
	disp.display()
	disp.clear()
	draw.rectangle((0,0,width,height), outline=0, fill=0)

