import os, glob
from pydub import AudioSegment

stress_keyword=['Fire']  # Give stress keywords
threshold = -18.5  # Stress finding threshold in dBFS

files = glob.glob('stress_sounds/*')
for f in files:
    print('removing '+ f)
    os.remove(f)

dataLog=[]
with open('decode.ctm','rt') as f:
    data = f.readlines()
for line in data:
    if line.__contains__(stress_keyword[0]): # Keyword for scream
        dataLog.append(line.strip('\n'))


cnt=1
for x in dataLog:
    y=x.split()
    # print(y[2], y[3])
    qs="ffmpeg -ss "+ y[2] +" -t "+ y[3] +" -i "+ "in_audio/"+y[0] +".wav stress_sounds/"+y[0]+ "_"+stress_keyword[0] +"_"+str(cnt)+"_stress.wav"
    os.system(qs)
    cnt +=1


# Printing only screaming or stressed wav names
arr = os.listdir('stress_sounds/')
for x in arr:
    # print(x)
    sound = AudioSegment.from_file("stress_sounds/"+ x, "wav")
    print(sound.dBFS)
    if (sound.dBFS >= threshold ):   # Stress finding threshold
        print('Found stress of '+stress_keyword[0]+ ' in : '+x)



exit (1)

# start to end cuttng
# os.system('ffmpeg -ss 4.920 -t 0.740 -i ben_010101.wav out.wav')