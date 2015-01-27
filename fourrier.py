import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import *
import math
import scipy

time=[]
accelX =[]
accelY =[]
accelZ =[]
accel=[]
freq=[]

def fillCollumn(file):
    global time
    global accelX
    global accelY
    global accelZ 
    f = np.loadtxt(file)
    time = copy(f[:,3])
    accelX=copy(f[:,0])
    accelY=copy(f[:,1])
    accelZ=copy(f[:,2])

def computeAccel():
    global accel
    a=0
    for i in range(0,len(accelX)):
        a=math.sqrt(pow(float(accelX[i]), 2) + pow(float(accelY[i]), 2) + pow(float(accelZ[i]), 2))
        accel.append(a)
   
def timeSet():
    global time
    beginning=time[0]
    for i in xrange(len(time)):
        time[i]-=beginning


def getFrequencies():
    global time
    global freq
    for i in range(0,len(time)):
        freq.append(time[i]/((1.)*len(time)))
   


fillCollumn('data_accel_co.txt')
computeAccel()

timeSet()
getFrequencies()
t = np.arange(250)
sp = np.fft.fft(accel)

#freq = np.fft.fftfreq(100)
sp=np.abs(sp)
plt.plot(freq, sp)
show()
