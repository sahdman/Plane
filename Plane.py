from Servo import *

class Plane:
	def __init__(self):
		# Servos connected to PWM pins of the Beagle Bone Black.
		# Edit this according to the plane connections.
		# Maximum number of servos allowed = 4
		self.Ailerons_Right = Servo("P8_13")
		self.Ailerons_Left  = Servo("P9_14")
		self.Flaps          = Servo("P9_21")
		self.Elevators      = Servo("P9_42")
		#self.Radar          = Servo("")
		
		self.Ailerons_Right.StartServo()
		self.Ailerons_Left.StartServo()
		self.Flaps.StartServo()
		self.Elevators.StartServo()
		
		# Set makimum titl angles of all servos.
		# Edit this portion according to the plane being used
		self.alireons_max  = 30
		self.falps_max     = 30
		self.elevators_max = 45
		self.radar_max = 45
		
		# Exponential componenet of the movement.
		# 1 - Linear, 
		self.alireons_exp  = 2
		self.elevators_exp = 2
		self.radar_exp     = 3
		
		# Throttle specific data
		self.engines = 1
	
	def MoveToInitial(self):
		self.Ailerons_Right.SetAngle(90)
		self.Ailerons_Left.SetAngle(90)
		self.Flaps.SetAngle(90)
		self.Elevators.SetAngle(90)
		#self.Radar.SetAngle(90)
	
	def TiltLeft(self, angle):
		self.Ailerons_Right.SetAngle(90 - angle)
		self.Ailerons_Left.SetAngle(90 + angle)
		
	def TiltRight(self, angle):
		self.Ailerons_Left.SetAngle(90 - angle)
		self.Ailerons_Right.SetAngle(90 + angle)
	
	def MakeVertical(self):
		self.Ailerons_Right.SetAngle(90)
		self.Ailerons_Left.SetAngle(90)
		self.Elevators.SetAngle(90)
		self.Flaps.SetAngle(90 + 30)
	
	def TiltPlane(self, joystick_angle):
		# A full joystic turn will correspond
		# to the servos being moved to the maximum
		# angle. joystick angle is form -1 - 1
		
		if joystick_angle == 0:
			return
		
		factor = 1
		for i in range(1, self.alireons_exp):
			factor = factor * i
		d_angle = factor * self.alireons_max;
		
		if d_angle > 0:
			# Turn right
			self.TiltRight(d_angle)
		else:
			self.TiltLeft(d_angle * -1)
			
	
	def LiftPlane(self, joystick_angle):
		# A full joystic turn will correspond
		# to the servos being moved to the maximum
		# angle. joystick angle is form -1 - 1
		
		if joystick_angle == 0:
			return
		
		factor = 1
		for i in range(1, self.elevators_exp):
			factor = factor * i
		d_angle = factor * self.elevators_max;
		
		self.Elevators.SetAngle(90 + d_angle)
	
	def OpenFlaps(self):
		self.Flaps.SetAngle(90 + 30)
	
	def CloseFlaps(self):
		self.Flaps.SetAngle(90)
	
	def MakeFall(self):
		self.Flaps.SetAngle(90 - 30)
	
	def Taxi(self, joystick_angle):
		# Not implements as only 4 servos supported
		print("Taxi")
	
	def SetThrottle(self, degree):
		# Not implememted
		print("THrottle")
	
    