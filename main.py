from Plane import *
from Servo import *
from Signal import *

def Loop():
	# Main application loop.
	global plane
	global signal
	
	# First receive Signal
	signal.ReceiveSignal()
	
	# Set the plane parameters
	plane.TiltPlane(signal.GetAilerons())
	plane.LiftPlane(signal.GetElevators())
	plane.Taxi(signal.GetRada())
	
	flaps = signal.GetFlaps()
	if flaps == 0:
		plane.CloseFlaps()
	else:
		plane.OpenFlaps()
	
	plane.SetThrottle(signal.GetThrottle())


def Initialize():
	global plane
	global signal
	
	print("Initializing the program")
	
	plane = Plane()
	signal = Signal()
	
	plane.MoveToInitial()
	plane.MakeVertical()
	
	# Sleep for adjustments to complete
	sleep(3)

if __name__ == "__main__":
	print("Starting the Plane application")
	
	# Initialize the program
	
	# Run the application loop
	print("Running the application loop")
	
	while 1:
		Loop()