import numpy as np
import plotly.express as px
import plotly.graph_objects as go


class FileReader():

    def __init__(self):
        self

    #
    # def mean(list):
    #     sum_num = 0
    #     for t in list:
    #         sum_num = sum_num + t
    #
    #     avg = sum_num / len(list)
    #     return avg

    # #Read durations
    def readDurations(self, durPath):
        f = open(durPath)
        durList = []
        for line in f:
            durList.append(float(line))

        print("durations were successfully read")
        return durList

    # #Read packet length
    def readPacketLengths(self, lenPath):
        f = open(lenPath)
        lengthsList = [[]]
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
    def readIntervals(self, intervalPath):
        f = open(intervalPath)
        intervalsList = [[]]
        sessionIntervalList = []
        for line in f:
            if line.isspace():
                intervalsList.append(sessionIntervalList)
                sessionIntervalList = []
            else:
                sessionIntervalList.append(float(line))
        print("intervals were successfully read")
        return intervalsList


# if __name__ == "__main__":
    # durPath = 'C:\Study\Programming\Python Projects\data\All sessions\\session duration.txt'
    # intervalPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet intervals in sessions.txt'
    # lenPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet lengths in sessions.txt'
    #
    # fileReader = FileReader()
    # durations = fileReader.readDurations(durPath)
    # intervals = fileReader.readIntervals(intervalPath)
    # lengths = fileReader.readPacketLengths(lenPath)
