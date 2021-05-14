import matplotlib.pyplot as plt
from fileReader import FileReader

durPath = 'C:\Study\Programming\Python Projects\data\All sessions\\session duration.txt'
intervalPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet intervals in sessions.txt'
lenPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet lengths in sessions.txt'
pathToSave = 'C:\Study\Programming\Python Projects\img\All sessions\\'
fileReader = FileReader()

durations = fileReader.readDurations(durPath)
intervals = fileReader.readIntervals(intervalPath)
lengths = fileReader.readPacketLengths(lenPath)

# Session length = sum of all packets lengths in session
sessionLengthsList = []
# Intensity = number of pkts / duration
intesities = []
# Packet nums in session
# pktNums = []
i = 0


for length in lengths:
    lengthSum = sum(length)
    sessionLengthsList.append(lengthSum)
    if durations.__getitem__(i) == 0:
        intesities.append(float(0))
    else:
        intesities.append(float(lengthSum/durations.__getitem__(i)))

    i += 1


plot1 = plt.figure(1)
plt.subplot(211)
plt.title("Session Lengths", fontsize=14, fontname='Times New Roman')
plt.ylabel("Length, bytes", fontsize=14, fontname='Times New Roman')
plt.scatter(durations, sessionLengthsList)

plt.subplot(212)
plt.ylabel("Length, bytes", fontsize=14, fontname='Times New Roman')
plt.xlabel("Duration, s", fontsize=14, fontname='Times New Roman')
plt.yscale('log')
plt.scatter(durations, sessionLengthsList)

plt.savefig(pathToSave + 'Length(duration).png')

plot2 = plt.figure(2)
plt.subplot(211)
plt.title("Session Intensity", fontsize=14, fontname='Times New Roman')
plt.ylabel("Intensity, bytes per second", fontsize=14, fontname='Times New Roman')
plt.scatter(durations, intesities)

plt.subplot(212)
plt.ylabel("Intensity, bytes per second", fontsize=14, fontname='Times New Roman')
plt.xlabel("Duration, s", fontsize=14, fontname='Times New Roman')
plt.yscale('log')
plt.scatter(durations, sessionLengthsList)

plt.savefig(pathToSave + 'Intensity(duration).png')
plt.show()

input()
