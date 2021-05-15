import matplotlib.pyplot as plt
from fileReader import FileReader

durPath = 'C:\Study\Programming\Python Projects\data\All sessions\\session duration.txt'
intervalPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet intervals in sessions.txt'
lenPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet lengths in sessions.txt'
pathToSave = 'C:\Study\Programming\Python Projects\img\All sessions\\'
fileReader = FileReader(durPath, intervalPath, lenPath)

durations = fileReader.getDurations()
lengths = fileReader.getLengths()
intervals = fileReader.getIntervals()
lengthPerSessionList = fileReader.getLengthsPerSession()
intensities = fileReader.getIntensities()

plot1 = plt.figure(1,figsize=(8,6))
plt.subplot(211)
plt.title("Session Lengths", fontsize=14, fontname='Times New Roman')
plt.ylabel("Length, bytes", fontsize=12, fontname='Times New Roman')
plt.scatter(durations, lengthPerSessionList)
plt.subplot(212)
plt.tight_layout(w_pad=0.5,h_pad=2.5)
plt.title("Session Length log scale", fontsize=14, fontname='Times New Roman')
plt.ylabel("Length, bytes", fontsize=12, fontname='Times New Roman',labelpad=0.5)
plt.xlabel("Duration, s", fontsize=12, fontname='Times New Roman',labelpad=1.1)
plt.yscale('log')
plt.scatter(durations, lengthPerSessionList)
plt.savefig(pathToSave + 'Length(duration).png')

# plot2 = plt.figure(2,figsize=(8, 6))
# plt.subplot(211)
# plt.title("Session Intensity", fontsize=14, fontname='Times New Roman')
# plt.ylabel("Intensity,\n bytes per second", fontsize=14, fontname='Times New Roman')
# plt.scatter(durations, intensities)
# plt.subplot(212)
# plt.tight_layout(w_pad=2,h_pad=2)
# plt.title("Session Intensity log scale", fontsize=14, fontname='Times New Roman')
# plt.ylabel("Intensity,\n bytes per second", fontsize=14, fontname='Times New Roman')
# plt.xlabel("Duration, s", fontsize=14, fontname='Times New Roman')
# plt.yscale('log')
# plt.scatter(durations, lengthPerSessionList)
# plt.savefig(pathToSave + 'Intensity(duration).png')
#
# # figsize has default float params 6 * 4 inches
# plot3 = plt.figure(3, figsize=(8, 4))
# plt.subplot(121)
# plt.title("Intensity(Length)", fontsize=14, fontname='Times New Roman')
# plt.xlabel("Length, bytes", fontsize=14, fontname='Times New Roman')
# plt.ylabel("Intensity,\n bytes per second", fontsize=14, fontname='Times New Roman')
# plt.scatter(lengthPerSessionList, intensities)
# plt.subplot(122)
# plt.title("Intensity(Length) log scale", fontsize=14, fontname='Times New Roman')
# plt.xlabel("Length, bytes", fontsize=14, fontname='Times New Roman')
# plt.xscale('log')
# plt.scatter(lengthPerSessionList, intensities)
# plt.savefig(pathToSave + 'Intensity(lengths).png')
# plt.tight_layout(h_pad=-0.88)

plt.show()

input()
