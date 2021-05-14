import numpy as np
import plotly.express as px
import plotly.graph_objects as go
def mean(list):
    sum_num = 0
    for t in list:
        sum_num = sum_num + t

    avg = sum_num / len(list)
    return avg

#Read durations
durPath = 'C:\Study\Programming\Python Projects\data\All sessions\\session duration.txt'
f = open(durPath)
durable = 0
durList = []
for line in f:
    durList.append(float(line))
    if float(line) > 61.0:
        durable += 1

maxDur = max(durList)
minDur = min(durList)
meanDur = mean(durList)

# print("Durable sessions number ", durable)
# print("maxDur = ", maxDur)
# print("minDur = ", minDur)
# print("meanDur = ", meanDur)
# print("list len = ", durList.__len__())

#Read packet length
lenPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet lengths in sessions.txt'
f = open(lenPath)
lengthsList = [[]]
sessionLenList = []
for line in f:
    if line.isspace():
        lengthsList.append(sessionLenList)
        sessionLenList = []
    else:
        sessionLenList.append(int(line))

print(lengthsList[lengthsList.__len__() - 1])

# Plots
x = []
y = []
