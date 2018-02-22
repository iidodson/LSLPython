# -*- coding: utf-8 -*-
import os,sys
from scipy import stats
import numpy as np

#Open file
with open('SNR.txt') as fh:
    electrode1 = fh.readlines()

#Remove white space and null values
electrode1 = [x.strip() for x in electrode1]
electrode1 = [x for x in electrode1 if x != 'nan']

#N=len(fh)-1
#for i in range(0,N):
#    try:
#        list1=[float(x) for x in electrode1]
#    except ValueError,e:
#        print "error",e,"on line",i
 
#k=[]
#for i in electrode1:
#    j = i.replace(' ','')
#    k.append

electrode1 = [x.strip(' ') for x in electrode1]

#[float(i) for i in electrode1]


#[float(i) if '.' in i else int(i) for i in electrode1]


#print(k) 
print "Max SNR for electrode1: ", max(electrode1)
print "Max SNR for electrode1: ", min(electrode1)


#bar = map(float, k

#with open('SNR2.txt') as fh2:
#    electrode2 = fh2.readlines()
#print(electrode1)
#e#lectrode2 = [x.strip() for x in electrode2]
#electrode2 = [x for x in electrode2 if x != 'nan'] 

#electrode1 = []
#electrode2 = []
#for i in content:
#    electrode1.append(i.split(None, 1)[0])

#for i in content:
#    electrode1.append(i.split(None, 1)[1])

#print "Max SNR for electrode1: ", max(bar)
#print "Min SNR electrode1: ", min(bar)
print "______________"
#print "Max SNR for electrode2: ", max(electrode2)
#print "Min SNR electrode2: ", min(electrode2)


fh.close()
#fh2.close()
