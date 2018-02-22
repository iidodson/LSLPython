"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream
import ps_drone
import time

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')


# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
print(inlet)

sample, timestamp= inlet.pull_sample()
val =  inlet.channel_count
print(val)

while True:
    	sample, timestamp= inlet.pull_sample()
    	#print(timestamp, sample)
	print(inlet)
	print (val)
	if val is None:
		print("not here")
    

    
    #print(sample)
    #print(streams)
    #print(inlet) 
