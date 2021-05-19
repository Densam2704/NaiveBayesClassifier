import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from fileReader import FileReader

class StaticVariables:
    figureNum = 1

class PlotMaker:
    fileReader = ""
    pathToSave = ""

    def __init__(self, fileReader, pathToSave):
        self.fileReader = fileReader
        self.pathToSave = pathToSave

    def make(self):
        self.makePlot1()
        self.makePlot2()
        self.makePlot3()

    # def makeFatDotPlot(self):
    #     durations = pd.DataFrame(self.fileReader.getDurations())
    #     lengthPerSessionList =pd.DataFrame(self.fileReader.getLengthsPerSession())
    #     df=pd.merge(durations,lengthPerSessionList,str ="full")
    #
    #     print(df[0])
    #     # fig,ax = plt.subplots(figsize=(8, 6),dpi=80)
    #     # sns.stripplot(durations,lengthPerSessionList,size=durations.size*2, ax=ax)
    #     # plt.title("Lengths (Duration)", fontsize=14, fontname='Times New Roman')
    #     #
    #     #
    #     # plt.savefig(self.pathToSave + 'Length(duration).png')
    #     # self.nextFigure()
    #     # self.showPlots()

    def makePlot1(self):
        durations = self.fileReader.getDurations()
        lengthPerSessionList = self.fileReader.getLengthsPerSession()
        pathToSave = self.pathToSave
        plot1 = plt.figure(StaticVariables.figureNum, figsize=(8, 6))
        plt.title("Lengths (Duration)", fontsize=14, fontname='Times New Roman')
        plt.ylabel("Length, bytes", fontsize=12, fontname='Times New Roman')
        plt.xlabel("Duration, s", fontsize=12, fontname='Times New Roman')
        plt.yscale('log')
        plt.scatter(durations, lengthPerSessionList)
        plt.savefig(pathToSave + 'Length(duration).png')

        self.nextFigure()

    def makePlot2(self):
        durations = self.fileReader.getDurations()
        intensities = self.fileReader.getIntensities()
        pathToSave = self.pathToSave

        plot2 = plt.figure(StaticVariables.figureNum, figsize=(8, 6))
        plt.title(" Intensity (Duration)", fontsize=14, fontname='Times New Roman')
        plt.ylabel("Intensity,\n bytes per second", fontsize=14, fontname='Times New Roman')
        plt.xlabel("Duration, s", fontsize=14, fontname='Times New Roman', labelpad=0.1)
        plt.yscale('log')
        plt.scatter(durations, intensities,color='r')
        plt.savefig(pathToSave + 'Intensity(duration).png')

        self.nextFigure()

    def makePlot3(self):
        lengthPerSessionList = self.fileReader.getLengthsPerSession()
        intensities = self.fileReader.getIntensities()
        pathToSave = self.pathToSave

        plot3 = plt.figure(StaticVariables.figureNum, figsize=(8, 4))
        plt.title("Intensity(Length)", fontsize=14, fontname='Times New Roman')
        plt.xlabel("Length, bytes", fontsize=14, fontname='Times New Roman')
        plt.ylabel("Intensity,\n bytes per second", fontsize=14, fontname='Times New Roman')
        plt.xscale('log')
        plt.scatter(lengthPerSessionList, intensities,color='g')
        plt.tight_layout(h_pad=-0.88)
        plt.savefig(pathToSave + 'Intensity(lengths).png')

        self.nextFigure()

    @staticmethod
    def showPlots(self):
            plt.show()

    def nextFigure(self):
        StaticVariables.figureNum+=1
        print(StaticVariables.figureNum)

# input()
