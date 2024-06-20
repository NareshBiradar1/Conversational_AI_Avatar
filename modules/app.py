import os
import cv2
import pygame
import threading
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog
from PIL import Image

from modules.gemini_response import GeminiResponse
from modules.speech_to_text import SpeechToText
from modules.Video_Audio_generation import generateVideo_and_audio

class VideoStreaming:
    def __init__(self, window, window_title, audio_source="audio.mp3", video_source="output.mp4", avatar_path="media/avatar.jpg"):
        self.video_source = video_source
        self.audio_source = audio_source
        self.avatar_source = avatar_path
        self.vid = None
        self.AVGen = generateVideo_and_audio(self.avatar_source)
        self.OpenAI = GeminiResponse()
        self.SpeechToText = SpeechToText()

        self.resize_width = 600
        self.resize_height = 600
        self.window = window
        self.window.title(window_title)

        self.canvas = Canvas(window, width=self.resize_width, height=self.resize_height)
        self.canvas.pack()

        self.entry = Entry(window, width=50)
        self.entry.pack(anchor=CENTER, pady=10)

        self.btn_send_message = Button(window, text="Ask the AI", width=50, command=self.send_message)
        self.btn_send_message.pack(anchor=CENTER, pady=10)

        self.btn_record_audio = Button(window, text="Record Audio", width=50, command=self.record_user_audio)
        self.btn_record_audio.pack(anchor=CENTER, pady=10)

        self.delay = 29
        self.show_image = True
        self.image = Image.open(self.avatar_source).resize((self.resize_width, self.resize_height))
        self.photo = ImageTk.PhotoImage(self.image)
        
        self.update_the_image()
        self.window.mainloop()

    def record_user_audio(self):
        duration = 5  # Length of recording in seconds
        fs = 44100  # Sample rate

        # Record audio
        print("Recording audio...")
        audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait for recording to finish

        # Save recorded audio to a file
        audio_path = "../recorded_audio.wav"
        wav.write(audio_path, fs, audio_data)

        # Transcribe recorded audio
        text = self.SpeechToText.transcribe(audio_path)

        if text:
            self.entry.delete(0, END)
            self.entry.insert(0, text)
        else:
            print("Error: Failed to transcribe audio")

    def play_the_audio(self, audio_path):
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

    def play_the_video(self):
        if not self.show_image:
            return
        self.show_image = False

        self.vid = cv2.VideoCapture(self.video_source)
        self.audio_thread = threading.Thread(target=self.play_the_audio, args=(self.audio_source,))
        self.audio_thread.start()
        self.update_the_video()

    def update_the_image(self):
        if self.show_image:
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

    def update_the_video(self):
        ret, frame = self.vid.read()

        if ret:
            frame = cv2.resize(frame, (self.resize_width, self.resize_height))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
            self.window.after(self.delay, self.update_the_video)
        else:
            self.show_image = True
            self.update_the_image()

    def send_message(self):
        self.__del__()

        message = self.entry.get()
        self.entry.delete(0, END)

        if message:
            response = self.OpenAI.get_gemini_response(message)
            if response and self.AVGen.text_to_video(response, audio_output=self.audio_source, video_output=self.video_source):
                self.play_the_video()
        else:
            print("Error: Empty message")

    def __del__(self):
        if self.vid and self.vid.isOpened():
            self.vid.release()
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            pass
        if os.path.exists(self.video_source):
            os.remove(self.video_source)
        if os.path.exists(self.audio_source):
            os.remove(self.audio_source)
