import Adafruit_BBIO.PWM as PWM

class Servo:
	
	def __init__(self, pin):
		self.servo_pin = pin
		self.duty_min = 3
		self.duty_max = 14.5
		self.duty_span = self.duty_max - self.duty_min
		
	def StartServo(self):
		PWM.start(self.servo_pin, (100-self.duty_min), 60.0, 1)
		self.current_angle = 90.0
		self.SetAngle(self.current_angle)
	
	def SetAngle(self, angle):
		print("Setting angle to - ")
		print(angle)
		angle_f = float(angle)
		duty = 100 - ((angle_f / 180) * self.duty_span + self.duty_min)
		PWM.set_duty_cycle(self.servo_pin, duty)
	
	def IncreaseAngle(self, angle):
		self.current_angle += angle
		self.SetAngle(self.current_angle)

	def DecreaseAngle(self, angle):
		self.current_angle -= angle
		self.SetAngle(self.current_angle)

	def StopServo(self):
		PWM.stop(self.servo_pin)
