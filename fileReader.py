
def mean(list):
    sum_num = 0
    for t in list:
        sum_num = sum_num + t

    avg = sum_num / len(list)
    return avg

path = 'C:\Study\Programming\Python Projects\data\All sessions\\session duration.txt'
f = open(path)
durList=[]
for line in f:
    durList.append(float(line))
    # print(durList.__len__())
maxDur=max(durList)
minDur=min(durList)
meanDur=mean(durList)

print("maxDur = ",maxDur)
print("minDur = ",minDur)
print("meanDur = ",meanDur)
print("list len = ",durList.__len__())



