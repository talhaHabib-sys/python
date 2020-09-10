import os
exten=(".txt",".mp3",".mp4",".csv",".wav",".png",".pdf")
for root,dirs,files in os.walk(os.curdir):
    for f in files:
        if(f.endswith(exten)):
            os.remove(f)
            print("removed!")
