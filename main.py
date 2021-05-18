from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# X, y = load_iris(return_X_y=True)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
# gnb = GaussianNB()
# y_pred = gnb.fit(X_train, y_train).predict(X_test)
# print("Number of mislabeled points out of a total %d points : %d"
#       % (X_test.shape[1], (y_test != y_pred).sum()))
from fileReader import FileReader
from plotMaker import PlotMaker

allDurPath = 'C:\Study\Programming\Python Projects\data\All sessions\\session duration.txt'
allIntervalPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet intervals in sessions.txt'
allLenPath = 'C:\Study\Programming\Python Projects\data\All sessions\\packet lengths in sessions.txt'
allPathToSave = 'C:\Study\Programming\Python Projects\img\All sessions\\'
telegramDurPath = 'C:\Study\Programming\Python Projects\data\Telegram\\telegram session duration.txt'
telegramIntervalPath = 'C:\Study\Programming\Python Projects\data\Telegram\\telegram packet intervals in sessions.txt'
telegramLenPath = 'C:\Study\Programming\Python Projects\data\Telegram\\telegram packet lengths in sessions.txt'
telegramPathToSave = 'C:\Study\Programming\Python Projects\img\Telegram\\'
discordDurPath = 'C:\Study\Programming\Python Projects\data\Discord\\discord session duration.txt'
discordIntervalPath = 'C:\Study\Programming\Python Projects\data\Discord\\discord packet intervals in sessions.txt'
discordLenPath = 'C:\Study\Programming\Python Projects\data\Discord\\discord packet lengths in sessions.txt'
discordPathToSave = 'C:\Study\Programming\Python Projects\img\Discord\\'

allReader = FileReader(allDurPath, allIntervalPath, allLenPath)
allPlotMaker = PlotMaker(allReader, allPathToSave)
allPlotMaker.make()

telegramReader = FileReader(telegramDurPath, telegramIntervalPath, telegramLenPath)
telegramPlotMaker = PlotMaker(telegramReader, telegramPathToSave)
telegramPlotMaker.make()

discordReader = FileReader(discordDurPath, discordIntervalPath, discordLenPath)
discordPlotMaker = PlotMaker(discordReader,discordPathToSave)
discordPlotMaker.make()

PlotMaker.showPlots(PlotMaker)