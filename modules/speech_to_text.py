
import speech_recognition as sr

class SpeechToText:       

    def transcribe(self, audio_file_path):
        
        try:
            r = sr.Recognizer()
            with sr.AudioFile(audio_file_path) as source:
                audio_data = r.record(source)
                text = r.recognize_google(audio_data)
                return text
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return None
