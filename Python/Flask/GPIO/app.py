from flask import Flask, render_template, request
import urllib
import urllib.request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

app = Flask(__name__)

msg = "null"

@app.route("/", methods=["GET", "POST"])
def index():
	global msg
	if request.method == 'POST':
		if request.form.get('greensubmit.x'):
			GPIO.output(17, GPIO.HIGH)
			GPIO.output(27, GPIO.LOW)
			msg = "GREENLEDHIGH"
		if  request.form.get('bluesubmit.x'):
			GPIO.output(17, GPIO.LOW)
			GPIO.output(27, GPIO.HIGH)
			msg = "BLUELEDHIGH"
	elif request.method == 'GET':
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		msg = "PAGE RELOADED"
	else:
		msg = "null"
	return render_template("index.html", msg=msg)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
