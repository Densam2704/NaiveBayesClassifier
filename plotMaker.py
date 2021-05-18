import matplotlib.pyplot as plt
from fileReader import FileReader

class FigureNum:
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

    def makePlot1(self):
        durations = self.fileReader.getDurations()
        lengthPerSessionList = self.fileReader.getLengthsPerSession()
        pathToSave = self.pathToSave
        plot1 = plt.figure(FigureNum.figureNum, figsize=(8, 6))
        plt.subplot(211)
        plt.title("Session Lengths", fontsize=14, fontname='Times New Roman')
        plt.ylabel("Length, bytes", fontsize=12, fontname='Times New Roman')
        plt.scatter(durations, lengthPerSessionList)
        plt.subplot(212)
        plt.title("Session Length log scale", fontsize=14, fontname='Times New Roman')
        plt.ylabel("Length, bytes", fontsize=12, fontname='Times New Roman')
        plt.xlabel("Duration, s", fontsize=12, fontname='Times New Roman')
        plt.yscale('log')
        plt.scatter(durations, lengthPerSessionList)
        plt.savefig(pathToSave + 'Length(duration).png')
        plt.tight_layout(h_pad=1)

        self.nextFigure()

    def makePlot2(self):
        durations = self.fileReader.getDurations()
        intensities = self.fileReader.getIntensities()
        pathToSave = self.pathToSave

        plot2 = plt.figure(FigureNum.figureNum, figsize=(8, 6))
        plt.subplot(211)
        plt.title("Session Intensity", fontsize=14, fontname='Times New Roman')
        plt.ylabel("Intensity,\n bytes per second", fontsize=14, fontname='Times New Roman')
        plt.scatter(durations, intensities, co)
        plt.subplot(212)
        plt.title("Session Intensity log scale", fontsize=14, fontname='Times New Roman')
        plt.ylabel("Intensity,\n bytes per second", fontsize=14, fontname='Times New Roman')
        plt.xlabel("Duration, s", fontsize=14, fontname='Times New Roman', labelpad=0.1)
        plt.yscale('log')
        plt.scatter(durations, intensities)
        plt.savefig(pathToSave + 'Intensity(duration).png')
        plt.tight_layout(h_pad=1)

        self.nextFigure()

    def makePlot3(self):
        lengthPerSessionList = self.fileReader.getLengthsPerSession()
        intensities = self.fileReader.getIntensities()
        pathToSave = self.pathToSave

        plot3 = plt.figure(FigureNum.figureNum, figsize=(8, 4))
        plt.subplot(121)
        plt.title("Intensity(Length)", fontsize=14, fontname='Times New Roman')
        plt.xlabel("Length, bytes", fontsize=14, fontname='Times New Roman')
        plt.ylabel("Intensity,\n bytes per second", fontsize=14, fontname='Times New Roman')
        plt.xscale('log')
        plt.scatter(lengthPerSessionList, intensities)
        plt.subplot(122)
        plt.title("Intensity(Length) log scale", fontsize=14, fontname='Times New Roman')
        plt.xlabel("Length, bytes", fontsize=14, fontname='Times New Roman')

        plt.scatter(lengthPerSessionList, intensities)
        plt.savefig(pathToSave + 'Intensity(lengths).png')
        plt.tight_layout(h_pad=-0.88)

        self.nextFigure()

    @staticmethod
    def showPlots(self):
            plt.show()

    def nextFigure(self):
        FigureNum.figureNum+=1
        print(FigureNum.figureNum)

# input()
