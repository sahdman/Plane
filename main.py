from Plane import *
from Servo import *
from Signal import *
import time

def Loop():
	# Main application loop.
	global plane
	global signal
	
	# First receive Signal
	signal.ReceiveSignal()
	
	# Set the plane parameters
	plane.TiltPlane(signal.GetAilerons())
	plane.LiftPlane(signal.GetElevators())
	plane.Taxi(signal.GetRadar())
	
	flaps = signal.GetFlaps()
	if flaps == 0:
		plane.CloseFlaps()
	else:
		plane.OpenFlaps()
	
	plane.SetThrottle(signal.GetThrottle())
	
	time.sleep(0.5)


def Initialize():
	global plane
	global signal
	
	print("=====> Initializing the program")
	
	plane = Plane()
	signal = Signal()
	
	print("Moving to initial positions")
	
	plane.MoveToInitial()
	plane.MakeVertical()
	
	# Sleep for adjustments to complete
	time.sleep(3)

if __name__ == "__main__":
	print("=====> Starting the Plane application")
	
	# Initialize the program
	Initialize()
	
	# Run the application loop
	print("=====> Running the application loop")
	
	while 1:
		Loop()