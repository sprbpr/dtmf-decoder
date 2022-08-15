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

    ######################################################################################

    n = np.linspace(0, RECORD_SECONDS, len(data))
    X = []
    F = [697, 770, 852, 941, 1209, 1336, 1477, 1633]
    for i in range(0, 8):
        X.append(complex(0, 0))
    # X_697 = complex(0, 0)
    # X_770 = complex(0, 0)
    # X_852 = complex(0, 0)
    # X_941 = complex(0, 0)
    # X_1209 = complex(0, 0)
    # X_1336 = complex(0, 0)
    # X_1477 = complex(0, 0)
    # X_1633 = complex(0, 0)

    for i in range(0, 8):
        index = 0
        for j in n:
            X[i] = X[i] + data[index] * np.exp(-1j * 2 * np.pi * F[i] * j)
            index = index + 1

    # index = 0
    # for i in n:
    #     X_697 = X_697 + data[index] * np.exp(-1j * 2 * np.pi * 697 * i)
    #     index = index + 1
    #
    # index = 0
    # for i in n:
    #     X_770 = X_770 + data[index] * np.exp(-1j * 2 * np.pi * 770 * i)
    #     index = index + 1
    #
    # index = 0
    # for i in n:
    #     X_852 = X_852 + data[index] * np.exp(-1j * 2 * np.pi * 852 * i)
    #     index = index + 1
    #
    # index = 0
        # for i in n:
    #     X_941 = X_941 + data[index] * np.exp(-1j * 2 * np.pi * 941 * i)
    #     index = index + 1
    #
    # index = 0
    # for i in n:
    #     X_1209 = X_1209 + data[index] * np.exp(-1j * 2 * np.pi * 1209 * i)
    #     index = index + 1
    #
    # index = 0
    # for i in n:
    #     X_1336 = X_1336 + data[index] * np.exp(-1j * 2 * np.pi * 1336 * i)
    #     index = index + 1
    #
    # index = 0
    # for i in n:
    #     X_1477 = X_1477 + data[index] * np.exp(-1j * 2 * np.pi * 1477 * i)
    #     index = index + 1
    #
    # index = 0
    # for i in n:
    #     X_1633 = X_1633 + data[index] * np.exp(-1j * 2 * np.pi * 1633 * i)
    #     index = index + 1

    # print(X_697.real * X_697.real + X_697.imag * X_697.imag)
    # print(X_770.real * X_770.real + X_770.imag * X_770.imag)
    # print(X_852.real * X_852.real + X_852.imag * X_852.imag)
    # print(X_941.real * X_941.real + X_941.imag * X_941.imag)
    # print(X_1209.real * X_1209.real + X_1209.imag * X_1209.imag)
    # print(X_1336.real * X_1336.real + X_1336.imag * X_1336.imag)
    # print(X_1477.real * X_1477.real + X_1477.imag * X_1477.imag)
    # print(X_1633.real * X_1633.real + X_1633.imag * X_1633.imag)
    #
    # print(X_697)
    # print(X_770)
    # print(X_852)
    # print(X_941)
    # print(X_1209)
    # print(X_1336)
    # print(X_1477)
    # print(X_1633)

    SafeFactor = 4

    XH = [abs(X[0]) * abs(X[0]), abs(X[1]) * abs(X[1]), abs(X[2]) * abs(X[2]), abs(X[3]) * abs(X[3])]
    XV = [abs(X[4]) * abs(X[4]), abs(X[5]) * abs(X[5]), abs(X[6]) * abs(X[6]), abs(X[7]) * abs(X[7])]

    XHPrime = [abs(X[0]) * abs(X[0]), abs(X[1]) * abs(X[1]), abs(X[2]) * abs(X[2]), abs(X[3]) * abs(X[3])]
    XVPrime = [abs(X[4]) * abs(X[4]), abs(X[5]) * abs(X[5]), abs(X[6]) * abs(X[6]), abs(X[7]) * abs(X[7])]

    XHPrime[XHPrime.index(max(XHPrime))] = -1
    XVPrime[XVPrime.index(max(XVPrime))] = -1

    if max(XH) > (SafeFactor * max(XHPrime)):
        if max(XV) > (SafeFactor * max(XVPrime)):
            if XH.index(max(XH)) == 0:
                if XV.index(max(XV)) == 0:
                    print(1)
                if XV.index(max(XV)) == 1:
                    print(2)
                if XV.index(max(XV)) == 2:
                    print(3)
                if XV.index(max(XV)) == 3:
                    print("A")
            if XH.index(max(XH)) == 1:
                if XV.index(max(XV)) == 0:
                    print(4)
                if XV.index(max(XV)) == 1:
                    print(5)
                if XV.index(max(XV)) == 2:
                    print(6)
                if XV.index(max(XV)) == 3:
                    print("B")
            if XH.index(max(XH)) == 2:
                if XV.index(max(XV)) == 0:
                    print(7)
                if XV.index(max(XV)) == 1:
                    print(8)
                if XV.index(max(XV)) == 2:
                    print(9)
                if XV.index(max(XV)) == 3:
                    print("C")
            if XH.index(max(XH)) == 3:
                if XV.index(max(XV)) == 0:
                    print("*")
                if XV.index(max(XV)) == 1:
                    print(0)
                if XV.index(max(XV)) == 2:
                    print("#")
                if XV.index(max(XV)) == 3:
                    print("D")
    #print(XV)
    #print(XH)

# for x in X:
#     print(abs(x) * abs(x))
# print("-----------------------------------------")
# print(max(XH))
# print(max(XV))
