#reset score

import pickle
scoreFile=open("scorefile.dat",'wb')
pickle.dump(0, scoreFile)
scoreFile.close()
