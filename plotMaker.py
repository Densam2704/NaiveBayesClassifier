import matplotlib.pyplot as plt
from fileReader import FileReader

durPath = 'C:\Study\Programming\Python Projects\data\All sessions\\session duration.txt'
intervalPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet intervals in sessions.txt'
lenPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet lengths in sessions.txt'
pathToSave = 'C:\Study\Programming\Python Projects\img\All sessions\\'
fileReader = FileReader(durPath, intervalPath, lenPath)

durations = fileReader.getDurations()
intervals = fileReader.getIntervals()
lengths = fileReader.getLengths()
lengthPerSessionList = fileReader.getLengthsPerSession()
intensities = fileReader.getIntensities()



plot1 = plt.figure(1)
plt.subplot(211)
plt.title("Session Lengths", fontsize=14, fontname='Times New Roman')
plt.ylabel("Length, bytes", fontsize=14, fontname='Times New Roman')
plt.scatter(durations, lengthPerSessionList)

plt.subplot(212)
plt.ylabel("Length, bytes", fontsize=14, fontname='Times New Roman')
plt.xlabel("Duration, s", fontsize=14, fontname='Times New Roman')
plt.yscale('log')
plt.scatter(durations, lengthPerSessionList)

plt.savefig(pathToSave + 'Length(duration).png')

plot2 = plt.figure(2)
plt.subplot(211)
plt.title("Session Intensity", fontsize=14, fontname='Times New Roman')
plt.ylabel("Intensity,\n bytes per second", fontsize=14, fontname='Times New Roman')
plt.scatter(durations, intensities)

plt.subplot(212)
plt.ylabel("Intensity,\n bytes per second", fontsize=14, fontname='Times New Roman')
plt.xlabel("Duration, s", fontsize=14, fontname='Times New Roman')
plt.yscale('log')
plt.scatter(durations, lengthPerSessionList)

plt.savefig(pathToSave + 'Intensity(duration).png')
plt.show()

input()
