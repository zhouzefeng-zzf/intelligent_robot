#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import re
import difflib
import pyaudio
import wave
import shutil
# import eyed3
# import wave
import os
import speech_recognition as sr
# from pydub import AudioSegment
import time
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

# speech record
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'record.wav'

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

shutil.copy(r"D:\NLTK_py\record.wav", r"D:\NLTK_py\guest_record")

# speech recognization
starttime = datetime.datetime.now()
i = 1
for name in os.listdir(r'D:\NLTK_py\guest_record'):
    sentence  = ''
    print("%d %s 开始转换" % (i, name))
    ##音频分块识别
    r = sr.Recognizer()
    # for i in range(kn):
    try:
        with sr.WavFile(r'D:\NLTK_py\guest_record\%s' % name) as source:
            audio = r.record(source)
            IBM_USERNAME = '38a755bd-1fe9-4a8d-bc30-10990c5e4bff'
            IBM_PASSWORD = '0t6WqX3iZw8E'
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='ja-JP')
            #ja-JP en-US
            print(text)
            sentence += text
            #open(r'D:\text\%s.txt' % name, 'a+').write(text)
            #time.sleep(5)
            #temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('%d %s 已完成' % (i, name))

            #   人名检测

            new_sentence = re.sub('\s', '', sentence)
            new_sentence = new_sentence.encode('utf-8')

            # for element in new_sentence:
            #    print element
            length = len(new_sentence) / 3
            print length
            name = ["田中", "佐藤", "鈴木","查无此人"]  # 日文格式

            ratio = 0
            for name1 in name:
                #print name1
                for i in range(length - 3):
                    print new_sentence[i * 3:(i + 3) * 3]
                    seq = difflib.SequenceMatcher(None, name1, new_sentence[i * 3:(i + 3) * 3])
                    ratio = seq.ratio()
                    print ratio
                    if ratio > 0.66:
                        break
                if ratio > 0.66:
                    break
            print "The recognized name is:  "
            print name1 + '\n'
            i = i+1

    except Exception as e:
        print(e)
        temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s %d %s 未完成' % (temptime, i, name))
        continue
jietime = datetime.datetime.now()
last=jietime-starttime
print('花费时间：%s'%last)



jietime = datetime.datetime.now()
last=jietime-starttime
print('花费时间：%s'%last)









