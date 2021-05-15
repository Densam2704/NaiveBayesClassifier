import numpy as np
import plotly.express as px
import plotly.graph_objects as go


class FileReader:
    durations = []
    lengths = []
    intervals = []
    intensities = []
    lengthsPerSession = []

    # def __init__(self):
    #     self

    def __init__(self,durPath,intervalPath,lengthPath):
        self.durations = self.readDurations(durPath)
        self.lengths = self.readPacketLengths(lengthPath)
        self.intervals = self.readIntervals(intervalPath)
        self.intensities = self.countIntensities()
        self.lengthsPerSession = self.countLengthsPerSession()

    #
    # def mean(list):
    #     sum_num = 0
    #     for t in list:
    #         sum_num = sum_num + t
    #
    #     avg = sum_num / len(list)
    #     return avg

    # Read durations
    @staticmethod
    def readDurations(durPath):
        f = open(durPath)
        durList = []
        for line in f:
            durList.append(float(line))

        print("durations were successfully read")
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
        print("lengths were successfully read")
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
        print("intervals were successfully read")
        return intervalsList

    # Intensity = sum packet lengths per session / duration
    def countIntensities(self):
        intensities = []
        i = 0

        for length in self.lengths:
            lengthSum = sum(length)
            if self.durations.__getitem__(i) == 0:
                intensities.append(float(0))
            else:
                intensities.append(float(lengthSum / self.durations.__getitem__(i)))
            i += 1

        print("intensities were counted")
        return intensities

    def countLengthsPerSession(self):
        sumLengthsList = []

        for length in self.lengths:
            sumLengthsList.append(sum(length))

        print("lengths per session were counted")
        return sumLengthsList



    # Getters
    def getDurations(self):
        return self.durations
    def getLengths(self):
        return self.lengths
    def getIntervals(self):
        return self.intervals
    def getIntensities(self):
        return self.intensities
    def getLengthsPerSession(self):
        return self.lengthsPerSession


# if __name__ == "__main__":
    # durPath = 'C:\Study\Programming\Python Projects\data\All sessions\\session duration.txt'
    # intervalPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet intervals in sessions.txt'
    # lenPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet lengths in sessions.txt'
    #
    # fileReader = FileReader()
    # durations = fileReader.readDurations(durPath)
    # intervals = fileReader.readIntervals(intervalPath)
    # lengths = fileReader.readPacketLengths(lenPath)
