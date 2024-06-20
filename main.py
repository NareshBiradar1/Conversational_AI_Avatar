from tkinter import Tk
from modules.app import VideoStreaming


if __name__ == "__main__":
    root = Tk()
    app = VideoStreaming(root, "AI Conversational Chatbot", video_source="media/video.mp4", audio_source="media/audio.mp3", avatar_path="media/avatar2.jpg")
    

