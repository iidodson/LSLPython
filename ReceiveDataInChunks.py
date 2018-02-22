# -*- coding: utf-8 -*-
"""Example program to demonstrate how to read a multi-channel time-series
from LSL in a chunk-by-chunk manner (which is more efficient)."""
from scipy.signal import butter, lfilter, lfilter_zi
import numpy as np
from pylsl import StreamInlet, resolve_stream

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
fs=125
inlet = StreamInlet(streams[0])
#
while True:
    # get a new sample (you can also omit the timestamp part if you're not    # interested in it)
    chunk, timestamps = inlet.pull_chunk()
    if timestamps:
	timestamps = np.asarray(timestamps)
	eegdata = np.asarray(chunk)
	winSampleLength, nbCh = eegdata.shape
#	print(eegdata.shape)
	w = np.hamming(winSampleLength)
    	dataWinCentered = eegdata - np.mean(eegdata, axis=0)  # Remove offset
    	dataWinCenteredHam = (dataWinCentered.T*w).T

    	#NFFT = nextpow2(winSampleLength)
	NFFT = 512
    	Y = np.fft.fft(dataWinCenteredHam, n=NFFT, axis=0)/winSampleLength
    	PSD = 2*np.abs(Y[0:int(NFFT/2), :])
    	f = fs/2*np.linspace(0, 1, int(NFFT/2))

    	# SPECTRAL FEATURES
    	# Average of band powers
    	# Delta <4
    	ind_delta = np.where(f < 4)
	meanDelta = np.mean(PSD[ind_delta, :], axis=0)
    	# Theta 4-8
    	ind_theta = np.where((f >= 4) & (f <= 8))
    	meanTheta = np.mean(PSD[ind_theta, :], axis=0)
    	# Alpha 8-12
    	ind_alpha = np.where((f >= 8) & (f <= 12))
    	meanAlpha = np.mean(PSD[ind_alpha, :], axis=0)
	maxAlpha = np.amax(PSD[ind_alpha, :], axis=0)
	SNR = maxAlpha/meanAlpha

    	# Beta 12-30
    	ind_beta = np.where((f >= 12) & (f < 30))
    	meanBeta = np.mean(PSD[ind_beta, :], axis=0)

    	feature_vector = np.concatenate((meanDelta, meanTheta, meanAlpha,
                                     meanBeta), axis=0)

#    	feature_vector = np.log10(feature_vector)
#	print(feature_vector)

	print(SNR[0])
	#print(SNR[0])
	print("\n")
	f=open('SNR.txt','ab')
	#np.savetxt(f, (np.transpose[SNR[3], SNR[6]])), fmt="%-f")
	np.savetxt(f, SNR[3], fmt="%f")

	g=open('SNR2.txt','ab')
        np.savetxt(g, SNR[6], fmt="%f")


  	 # SNRAsList = SNR.tolist()
    	#fh = open("SNR.txt", 'w')
	#for i in range(len(SNR)):
	#fh.write("\n".join(SNR))
        #	file.write(SNR[i])

   	#fh.close()
	#file.write(SNR[0])
