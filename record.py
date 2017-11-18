#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pyaudio
import wave
from array import array


FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024
RECORD_SECONDS=15
FILE_NAME="RECORDING.wav"

audio=pyaudio.PyAudio() #instantiate the pyaudio

#recording prerequisites
stream=audio.open(format=FORMAT,channels=CHANNELS, 
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)

#starting recording
frames=[]
flag =0
speak_num = 0
record_flag = 0
listNoSpeak = [1]*70
for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
    data=stream.read(CHUNK)
    data_chunk=array('h',data)
    vol=max(data_chunk)
    if(vol>=800):
        if (record_flag ==0):
            print ('*recording start*')
        record_flag = 1
    if(sum(listNoSpeak) !=0 and  record_flag==1):
        frames.append(data)
    if(flag ==0):
        if(vol>=500):
            print("something said")
            del listNoSpeak[0]
            listNoSpeak.append(1)
            print listNoSpeak
        #frames.append(data)
            speak_num = speak_num+1
        if (speak_num>=43):
            flag = 1
            listNoSpeak = [1] * 70
    else :
        if(vol<500):
            print("nothing")
            del listNoSpeak[0]
            listNoSpeak.append(0)
            print listNoSpeak
        # nospeak_num  = nospeak_num+1
        print sum(listNoSpeak)
        if(flag==1 and sum(listNoSpeak)==0):
            print('recording over')
            break

    print("\n")
    print i
    print flag
    
    
#end of recording
stream.stop_stream()
stream.close()
audio.terminate()
#writing to file
wavfile=wave.open(FILE_NAME,'wb')
wavfile.setnchannels(CHANNELS)
wavfile.setsampwidth(audio.get_sample_size(FORMAT))
wavfile.setframerate(RATE)
wavfile.writeframes(b''.join(frames))#append frames recorded to file
wavfile.close()
