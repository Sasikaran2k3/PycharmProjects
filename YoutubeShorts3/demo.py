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

date = "".join(str(datetime.date.today()).split("-"))
audio = AudioFileClip(os.path.dirname(__file__) + "\\Data\\%s.mp3" % date)
back = AudioFileClip(os.path.dirname(__file__) + "\\Background.mp3")
divider = audio.duration / 4
#img1 = ImageClip(os.path.dirname(__file__) + "\\Data\\%s.png" % date).set_duration(divider)
final = []
for i in range(4):
    img = ImageClip(os.path.dirname(__file__) + "\\Data\\%s_%d.png" % (date, i))
    img = img.resize(height=1920, width=1080)
    img = img.set_duration(divider)
    img = fadein(img,1.5)
    final .append(img)

out = concatenate(final, method="compose").write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % date, fps=24)
out.set_audio(CompositeAudioClip([audio, back]))
out.write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % (date),fps=24)

"""img = ImageClip(os.path.dirname(__file__) + "\\Data\\%s_%d.png" % (date,0)).set_duration(divider)
img1.resize(height=1080, width=1920)
img.resize(height=1080, width=1920)
i1 = fadein(img,2.0)
i2 = fadein(img1, 2.0)
final = [i1, i2]
#concatenate_videoclips(final,method="compose").write_videofile(os.path.dirname(__file__) + "\\Data\\%s_demo.mp4" % (date),fps=24)
for i in range(3):
    print(os.path.dirname(__file__) + "\\Data\\%s_%d.png" % (date,i))
    img = ImageClip(os.path.dirname(__file__) + "\\Data\\%s_%d.png" % (date,i)).set_duration(divider)
    #vid = concatenate_videoclips([img])#.resize(height=1920, width=1080)
    #vid.duration = divider
    #vid = vid.crossfadein(3.0)
    #vid.fps = 24
    #vid.resize(height=1920, width=1080).crossfadein(5.0)
    #vid.crossfadein(5.0)
    #vid.write_videofile(os.path.dirname(__file__) + "\\Data\\%s_%d.mp4" % (date,i),fps=24)
    final.append(fadein(ImageClip(os.path.dirname(__file__) + "\\Data\\%s_%d.png" % (date,i)).set_duration(divider).resize(height=1920, width=1080),2.0))
print(final)
for i in range(len(final)):
    print(final[i])
f = concatenate_videoclips(final)
#f.write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % (date),fps=24)
concatenate(final, method="compose").write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % (date),fps = 24)
"""