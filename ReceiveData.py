"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream
import ps_drone
import time

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')


# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

#Cresting drone instance and starting drone
drone = ps_drone.Drone()
drone.startup()

# Start drone
drone.trim() 
time.sleep(1) 
drone.takeoff()
time.sleep(3)

while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
   sample = 0
    sample, timestamp= inlet.pull_sample()
    if len(sample) >  0
        print("Recieving EEG Data")
    if sample  :
        drone.stop()
        time.sleep(1)
        drone.land()
    else:
        if sample[1] < 0:
            drone.hover()
   # print(sample[1])
