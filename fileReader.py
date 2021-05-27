import numpy as np
import plotly.express as px
import plotly.graph_objects as go


class FileReader:
    fileGroupName = ""
    durations = []
    packetLengths = []
    intervals = []
    intensities = []
    sessionLengths = []
    packetNums = []
    throughputs = []

    # def __init__(self):
    #     self
    def __init__(self, fileGroupName, durPath, intervalPath, lengthPath):
        self.fileGroupName = fileGroupName
        self.durations = self.readDurations(durPath)
        self.packetLengths = self.readPacketLengths(lengthPath)
        self.intervals = self.readIntervals(intervalPath)
        self.packetNums = self.countPacketNums()
        self.intensities = self.countIntensities()
        self.sessionLengths = self.countSessionLengths()

        self.throughputs = self.countThroughputs()

    # def __init__(self, durPath, intervalPath, lengthPath):
    #     self.durations = self.readDurations(durPath)
    #     self.packetLengths = self.readPacketLengths(lengthPath)
    #     self.intervals = self.readIntervals(intervalPath)
    #     self.intensities = self.countIntensities()
    #     self.sessionLengths = self.countSessionLengths()
    #     self.packetNums = self.countPacketNums()

    # Count packet number in each session
    def countPacketNums(self):
        packetNums = []
        for interval in self.intervals:
            packetNums.append(interval.__len__())
        # print("packet numbers were successfully counted")
        return packetNums

    # Read durations
    @staticmethod
    def readDurations(durPath):
        f = open(durPath)
        durList = []
        for line in f:
            durList.append(float(line))

        # print("durations were successfully read")
        return durList

    # Read packet length
    @staticmethod
    def readPacketLengths(lenPath):
        f = open(lenPath)
        lengthsList = []
        sessionLenList = []
        for line in f:
            if line.isspace():
                lengthsList.append(sessionLenList)
                sessionLenList = []
            else:
                sessionLenList.append(int(line))
        # print("lengths were successfully read")
        return lengthsList

    # Read intervals (inter packet times)
    @staticmethod
    def readIntervals(intervalPath):
        f = open(intervalPath)
        intervalsList = []
        sessionIntervalList = []
        for line in f:
            if line.isspace():
                intervalsList.append(sessionIntervalList)
                sessionIntervalList = []
            else:
                sessionIntervalList.append(float(line))
        # print("intervals were successfully read")
        return intervalsList

    # Intensity = packetNums / duration
    def countIntensities(self):
        intensities = []
        i = 0

        for packetNum in self.packetNums:
            if self.durations.__getitem__(i) == 0:
                intensities.append(float(0))
            else:
                intensities.append(float(int(packetNum) / self.durations.__getitem__(i)))
            i += 1

        return intensities

    # Throughput = sum packet lengths per session / duration
    def countThroughputs(self):
        throughputs = []
        i = 0
        for length in self.packetLengths:
            lengthSum = sum(length)
            if self.durations.__getitem__(i) == 0:
                throughputs.append(float(0))
            else:
                throughputs.append(float(lengthSum / self.durations.__getitem__(i)))
            i += 1

        return throughputs

    def countSessionLengths(self):
        sumLengthsList = []

        for length in self.packetLengths:
            sumLengthsList.append(sum(length))

        # print("lengths per session were counted")
        return sumLengthsList

    # Getters
    def getFileGroupName(self):
        return str(self.fileGroupName)

    def getDurations(self):
        return self.durations

    def getPacketLengths(self):
        return self.packetLengths

    def getIntervals(self):
        return self.intervals

    def getIntensities(self):
        return self.intensities

    def getSessionLengths(self):
        return self.sessionLengths

    def getPacketNums(self):
        return self.packetNums

    def getThroughputs(self):
        return self.throughputs

# if __name__ == "__main__":
# durPath = 'C:\Study\Programming\Python Projects\data\All sessions\\session duration.txt'
# intervalPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet intervals in sessions.txt'
# lenPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet lengths in sessions.txt'
#
# fileReader = FileReader()
# durations = fileReader.readDurations(durPath)
# intervals = fileReader.readIntervals(intervalPath)
# lengths = fileReader.readPacketLengths(lenPath)
