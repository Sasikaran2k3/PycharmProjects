import time
import os
import datetime
from moviepy.editor import *
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video import VideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.fx.fadein import fadein


date = "20230804"#.join(str(datetime.date.today()).split("-"))
audio = AudioFileClip(os.path.dirname(__file__) + "\\Data\\%s.mp3" % date)
back = AudioFileClip(os.path.dirname(__file__) + "\\Background.mp3")
divider = audio.duration / 8
#img1 = ImageClip(os.path.dirname(__file__) + "\\Data\\%s.png" % date).set_duration(divider)
final = []
for i in range(8):
    pic_num = i%4
    print(pic_num)
    img = ImageClip(os.path.dirname(__file__) + "\\Data\\%s_%d.png" % (date, pic_num))
    img = img.resize(height=1080, width=1920)
    img = img.set_duration(divider)
    img = fadein(img,1.5)
    final .append(img)
out = concatenate(final, method="compose")#.write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % date, fps=24)
out = out.set_audio(CompositeAudioClip([audio, back]))
out.duration = divider*8 + 1
print(out.duration)
out_len = divider*8 + 1
out = out.subclip(0, out_len)
out.write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % date, fps=24)
