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

print(durations.__len__())
x = durations
y = []
for length in lengths:
    y.append(sum(length))
y.__delitem__(0)

# subplot(x1,x2,x3)
# Первое определяет количество частей, на которое нужно разбить объект по вертикали.
# Второе — горизонтальное разделение.
# А третье число указывает на текущий подграфик, для которого будут актуальны команды.
plot1 = plt.figure(1)

plt.title("Session Lengths", fontsize=14, fontname='Times New Roman')
plt.xlabel("Duration, s", fontsize=14, fontname='Times New Roman')
plt.ylabel("Length, bytes", fontsize=14, fontname='Times New Roman')
plt.scatter(x, y)
plt.savefig(pathToSave+'Length(duration).png')


plot2 = plt.figure(2)
plt.title("Session Intensity", fontsize=14, fontname='Times New Roman')
plt.xlabel("Duration, s", fontsize=14, fontname='Times New Roman')
plt.ylabel("Length, bytes", fontsize=14, fontname='Times New Roman')
plt.scatter(x, y)
plt.savefig(pathToSave+'Intensity(duration).png')

plt.show()

input()
