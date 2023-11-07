import os
import time
import datetime
import moviepy.editor as mp
import speech_recognition as sr

date = "".join(str(datetime.date.today()).split("-"))

# Load the MP3 audio file
audio_file = (os.path.dirname(__file__)+"/Data/"+date+".mp3")  # Replace with your MP3 file path
print(audio_file)

video = mp.AudioFileClip(audio_file)

# Initialize the recognizer
recognizer = sr.Recognizer()

# Transcribe the audio
audio_text = recognizer.recognize_google(audio_file)

# Split the text into sentences
sentences = audio_text.split('.')

# Create an SRT-like output with timestamps
srt_output = ""
for i, sentence in enumerate(sentences):
    start_time = i * video.duration / len(sentences)
    end_time = (i + 1) * video.duration / len(sentences)
    srt_output += f"{i + 1}\n{start_time:.3f} --> {end_time:.3f}\n{sentence.strip()}\n\n"

# Save the SRT-like output to a file
with open("output.srt", "w") as srt_file:
    srt_file.write(srt_output)
