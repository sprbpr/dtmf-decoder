#!/usr/bin/env python3
from scipy.io import wavfile as wav
import pyaudio
import wave
import numpy as np

while True:
    FORMAT = pyaudio.paInt16  # format of sampling 16 bit int
    CHANNELS = 1  # number of channels it means number of sample in every sampling
    RATE = 44100  # number of sample in 1 second sampling
    CHUNK = 1024  # length of every chunk
    RECORD_SECONDS = 1  # time of recording in seconds
    WAVE_OUTPUT_FILENAME = "file.wav"  # file name

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    # print("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # print("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # storing voice
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    # reading voice
    rate, data = wav.read('file.wav')
    # data is voice signal. its type is list(or numpy array)

    # -----------------------------------------------------------------------------------

    F = [697, 770, 852, 941, 1209, 1336, 1477, 1633]
    # array of frequencies which must be checked

    Range = 10
    # the range of frequencies near original frequencies

    X_697 = []
    X_770 = []
    X_852 = []
    X_941 = []
    X_1209 = []
    X_1336 = []
    X_1477 = []
    X_1633 = []
    # arrays of near FT frequencies of original frequencies

    for i in range(F[0] - Range, F[0] + Range):
        X_697.append(abs(np.fft.fft(data))[i])

    for i in range(F[1] - Range, F[1] + Range):
        X_770.append(abs(np.fft.fft(data))[i])

    for i in range(F[2] - Range, F[2] + Range):
        X_852.append(abs(np.fft.fft(data))[i])

    for i in range(F[3] - Range, F[3] + Range):
        X_941.append(abs(np.fft.fft(data))[i])

    for i in range(F[4] - Range, F[4] + Range):
        X_1209.append(abs(np.fft.fft(data))[i])

    for i in range(F[5] - Range, F[5] + Range):
        X_1336.append(abs(np.fft.fft(data))[i])

    for i in range(F[6] - Range, F[6] + Range):
        X_1477.append(abs(np.fft.fft(data))[i])

    for i in range(F[7] - Range, F[7] + Range):
        X_1633.append(abs(np.fft.fft(data))[i])
    # append elements to above arrays

    x_697 = max(X_697)
    x_770 = max(X_770)
    x_852 = max(X_852)
    x_941 = max(X_941)
    x_1209 = max(X_1209)
    x_1336 = max(X_1336)
    x_1477 = max(X_1477)
    x_1633 = max(X_1633)
    # find maximum of above X_is arrays and put them in x_is

    XV = [x_697 * x_697, x_770 * x_770, x_852 * x_852, x_941 * x_941]
    XH = [x_1209 * x_1209, x_1336 * x_1336, x_1477 * x_1477, x_1633 * x_1633]
    # divide x_is by horizontal and vertical frequencies

    XVPrime = [x_697 * x_697, x_770 * x_770, x_852 * x_852, x_941 * x_941]
    XHPrime = [x_1209 * x_1209, x_1336 * x_1336, x_1477 * x_1477, x_1633 * x_1633]
    # make other arrays as same as XH and XV just for finding second maximum

    XVPrime[XVPrime.index(max(XVPrime))] = -1
    XHPrime[XHPrime.index(max(XHPrime))] = -1
    # find maximum of XHPrime and XVPrime arrays and change them to -1 to find second maximum

    SafeFactor = 4
    # we need a coefficient to determine whether a button has been pressed

    # if max(XH) is bigger than SafeFactor * max(XHPrime)
    # it means that some element in XH is significantly bigger than others

    # if max(XV) is bigger than SafeFactor * max(XVPrime)
    # it means that some element in XV is significantly bigger than others

    if max(XV) > (SafeFactor * max(XVPrime)):
        if max(XH) > (SafeFactor * max(XHPrime)):
            if XV.index(max(XV)) == 0:
                if XH.index(max(XH)) == 0:
                    print(1)
                if XH.index(max(XH)) == 1:
                    print(2)
                if XH.index(max(XH)) == 2:
                    print(3)
                if XH.index(max(XH)) == 3:
                    print("A")
            if XV.index(max(XV)) == 1:
                if XH.index(max(XH)) == 0:
                    print(4)
                if XH.index(max(XH)) == 1:
                    print(5)
                if XH.index(max(XH)) == 2:
                    print(6)
                if XH.index(max(XH)) == 3:
                    print("B")
            if XV.index(max(XV)) == 2:
                if XH.index(max(XH)) == 0:
                    print(7)
                if XH.index(max(XH)) == 1:
                    print(8)
                if XH.index(max(XH)) == 2:
                    print(9)
                if XH.index(max(XH)) == 3:
                    print("C")
            if XV.index(max(XV)) == 3:
                if XH.index(max(XH)) == 0:
                    print("*")
                if XH.index(max(XH)) == 1:
                    print(0)
                if XH.index(max(XH)) == 2:
                    print("#")
                if XH.index(max(XH)) == 3:
                    print("D")

    # check which element is significantly bigger than others and determine
    # which button has been pressed and print it


