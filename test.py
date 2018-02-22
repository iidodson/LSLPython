import ps_drone
import time

drone = ps_drone.Drone()
drone.startup()

print("Drone started...Would you like to take off y/n?")

usr = raw_input("-> ")

if(usr == 'y'):
	drone.trim()
	time.sleep(1)
	drone.takeoff()
	time.sleep(3)
	drone.hover()
	time.sleep(10)
	drone.turnLeft(1)
	time.sleep(3)
	drone.turnRight(1)
	time.sleep(3)
	drone.land()

