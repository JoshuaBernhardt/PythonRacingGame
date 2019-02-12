def loadScore():
    import pickle
    scoreFile=open(("scorefile.dat"),'rb')
    totalScore=pickle.load(scoreFile)
    scoreFile.close()
    writeScore(totalScore)

def writeScore(totalScore):
    import pickle
    scoreFile=open(("scorefile.dat"),'wb')
    totalScore+=5
    pickle.dump(totalScore, scoreFile)
    scoreFile.close()
    readScore()

def readScore():
    import pickle
    scoreFile=open(("scorefile.dat"),'rb')
    print(pickle.load(scoreFile))


                
def reset():
    import pickle
    scoreFile=open(("scorefile.dat"),'wb')
    pickle.dump(0,scoreFile)
    scoreFile.close()






    
