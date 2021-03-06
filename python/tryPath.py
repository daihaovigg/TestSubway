import datetime

class TryPath():
    def __init__(self,tts,ww):
        self.tts = tts
        self.walkIn = ww

    def dpkPath(self,x):
        L = x.split(',')
        starttime = self.addWalkTime(L[1],L[2])
        res = L[:7]
        isstart = True
        for i in range(7,len(L) - 1):
            starttime,endtime = self.tts.getEndTime(L[i],L[i+1],starttime,isstart)
            isstart = False
            res.append(L[i])
            res.append(L[i+1])
            res.append(starttime)
            res.append(endtime)
            starttime = endtime
        ress = ','.join(res)
        return ress

    def addWalkTime(self,station,s):
        fmt = "%H:%M:%S"
        dd = datetime.datetime.strptime(s,fmt)
        wl = datetime.timedelta(seconds = self.walkIn[station])
        return datetime.datetime.strftime(dd+wl,fmt)

    def getAllPath(self,data):
        return data.map(self.dpkPath)


