import datetime
import os

from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip

i=1
date = "".join(str(datetime.date.today()).split("-")) + "_"
audio = AudioFileClip(os.path.dirname(__file__) + "\\Data\\%s.mp3" % (date+str(i)))
back = AudioFileClip("Background.mp3")
image = ImageClip(os.path.dirname(__file__) + "\\Data\\%s.png" % (date+str(i)))
video = image.set_audio(CompositeAudioClip([audio,back]))
audio_duration = audio.duration + 1
print(audio_duration)
video.duration = audio_duration
video.fps = 1
video = video.subclip(0,audio_duration)
video.write_videofile(os.path.dirname(__file__) + "\\Data\\Demo.mp4" )