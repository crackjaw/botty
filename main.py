import pylab as plt
import time

rawData = open("sessions_data.txt", "r+")

rawList = []

times = []
valA = []
valB = []

for i in rawData.read().split('\n'):
    splitI = i.split("\t")
    splitI[0] = splitI[0]
    times.append(time.mktime(time.strptime(splitI[0][0:19], "%Y-%m-%dT%H:%M:%S")))
    valA.append(int(splitI[1].strip(" ").replace(",", "")))
    valB.append(int(splitI[3].strip(" ").replace(",", "")))

print(times)
print(valA)
print(valB)
    
plt.figure('Sessions', figsize=(16,8))
plt.clf()
plt.plot(times, valA,  'b-', linewidth = 2.0)
plt.plot(times, valB, 'b-', linewidth = 2.0)
plt.ticklabel_format(style="plain")
plt.show()