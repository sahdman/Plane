class Signal:
	def __init__(self):
		self.ailerons = 0
		self.elevators = 0
		self.flaps = 0
		self.radar = 0
		
		self.bomb = 0
		
		self.throttle = 0
	
	def ReceiveSignal(self):
		# Implement the communication specific code here.
		print("Receiving Signal data")
	
	def GetAilerons(self):
		return self.ailerons
	
	def GetElevators(self):
		return self.elevators
	
	def GetFlaps(self):
		return self.flaps
	
	def GetRadar(self):
		return self.radar
	
	def GetThrottle(self):
		return self.throttle
	
	def GetBomb(self):
		return self.bomb
	
