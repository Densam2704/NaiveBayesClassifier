from fileReader import FileReader


class Statistics:
    fileReader = []

    def __init__(self, fileReader):
        self.fileReader = fileReader
        self.make()

    def make(self):
        print("\nStats for " + self.fileReader.getFileGroupName())
        self.printStats("Durations", "s", self.fileReader.getDurations())
        self.printStats("Packet Numbers", "packets", self.fileReader.getPacketNums())
        self.printStats("Session Lengths", "bytes", self.fileReader.getSessionLengths())
        self.printStats("Intensities", "1/s", self.fileReader.getIntensities())
        self.printStats("Throughputs", "bytes/s", self.fileReader.getIntensities())

    def printStats(self, statName, units, list):
        print(statName + " Max = " + str(max(list)) + " " + units)
        print(statName + " Min = " + str(min(list)) + " " + units)
        print(statName + " Min not zero = " + str(self.minNotZero(list)) + " " + units)
        print(statName + " Avg = " + str(self.average(list)) + " " + units)

    def minNotZero(self, list):
        min = float(1000000)
        for element in list:
            if (float(element) < min and float(element) != 0.0):
                min = float(element)
        return min

    def average(self, list):
        sum_num = 0
        for t in list:
            sum_num = sum_num + t

        avg = sum_num / len(list)
        return avg
